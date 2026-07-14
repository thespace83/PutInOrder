from analyzer import Applicant
from os.path import join

applicants: set = set()


def check_titles(title: str) -> bool:
    titles: list[str] = title[1:-1].split(';')
    return (titles[0] == '"Порядковый номер"' and titles[1] == '"ID участника"' and titles[2] == '"Приоритет конкурса"'
            and titles[3] == '"Подано согласие"' and titles[4] == '"Сумма баллов"' and titles[5] == '"Баллы за ВИ"'
            and titles[6] == '"Баллы за ИД"' and titles[7] == '"Статус"' and titles[
                8] == '"Дата выбора конкурсной группы по Москве"')


def parse_applicant(row: str, referral: str) -> Applicant | None:
    data: list[str] = row[:-1].split(';')
    consent_submitted: bool = False if data[3] == '"—"' else True
    if not consent_submitted:
        return None

    uuid = int(data[1])
    priority: int = int(data[2])
    amount_of_points = int(data[4])

    for applicant in applicants:
        if applicant.uuid == uuid:
            applicant.priorities[referral] = priority
            return applicant

    return Applicant(uuid, {referral: priority}, amount_of_points)


def parse_referral(path: str, name: str) -> set[Applicant]:
    result: set[Applicant] = set()

    file = open(path, 'rb')
    if not check_titles(file.readline().decode('utf-8')):
        raise 'Не верный .csv файл!'

    for row in file.readlines():
        applicants.add(parse_applicant(row.decode('utf-8'), name))

    return result


def parse_university() -> dict[str, set[Applicant]]:
    university: dict[str, set[Applicant]] = {}
    referrals: list[str] = [
        'Уголовное_право, криминалистика и уголовное судопроизводство_Цивилистика_и гражданское судопроизводство.2026-07-14_13-21-04',
        'Финансы_и кредит.2026-07-14_13-21-05']

    for referral in referrals:
        university[referral] = parse_referral(join('parser', 'data', f'{referral}.csv'), referral)

    return university
