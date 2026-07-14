from analyzer import Applicant
from os.path import join


def check_titles(title: str) -> bool:
    titles: list[str] = title[1:-1].split(';')
    print(titles)
    return (titles[0] == '"Порядковый номер"' and titles[1] == '"ID участника"' and titles[2] == '"Приоритет конкурса"'
            and titles[3] == '"Подано согласие"' and titles[4] == '"Сумма баллов"' and titles[5] == '"Баллы за ВИ"'
            and titles[6] == '"Баллы за ИД"' and titles[7] == '"Статус"' and titles[
                8] == '"Дата выбора конкурсной группы по Москве"')


def parse_applicant(row: str) -> Applicant:
    data: list[str] = row[:-1].split(';')
    uuid = int(data[1])
    priority: int = int(data[2])
    consent_submitted: bool = False if data[3] == '"—"' else True
    amount_of_points = int(data[4])

    return Applicant(uuid, priority, consent_submitted, amount_of_points)


def parse_referral(path: str) -> set[Applicant]:
    result: set[Applicant] = set()

    referral = open(path, 'rb')
    if not check_titles(referral.readline().decode('utf-8')):
        raise 'Не верный .csv файл!'

    for row in referral.readlines():
        result.add(parse_applicant(row.decode('utf-8')))

    return result


def get_applicants(university: dict[str, set[Applicant]]) -> set[Applicant]:
    applicants: set = set()
    for referral in university.keys():
        for target in university[referral]:
            is_in: bool = False
            for applicant in applicants:
                if applicant.uuid == target.uuid:
                    is_in = True
            if not is_in:
                applicants.add(target)

    return applicants


def parse_university() -> dict[str, set[Applicant]]:
    university: dict[str, set[Applicant]] = {}
    files: list[str] = [
        'Уголовное_право, криминалистика и уголовное судопроизводство_Цивилистика_и гражданское судопроизводство.2026-07-14_13-21-04.csv',
        'Финансы_и кредит.2026-07-14_13-21-05.csv']
    for file in files:
        university[file] = parse_referral(join('parser', 'data', file))

    return university
