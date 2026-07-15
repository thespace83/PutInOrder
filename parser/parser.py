from analyzer import Applicant, Referral
from os.path import join

applicants: set = set()


def check_titles(title: str) -> bool:
    titles: list[str] = title[:-1].split(';')
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


def parse_referral(path: str, name: str, number_of_places: int) -> Referral:
    referral: Referral = Referral(name, number_of_places)

    file = open(path, 'rb')
    if not check_titles(file.readline().decode('utf-8')):
        raise 'Не верный .csv файл!'

    for row in file.readlines():
        applicant = parse_applicant(row.decode('utf-8'), name)
        if applicant:
            referral.applicants.add(applicant)

    return referral


def parse_university() -> dict[str, Referral]:
    university: dict[str, Referral] = {}
    referrals: list[tuple[str, int]] = [
        ('Спец. #A', 3),
        ('Спец. #B', 2),
        ('Спец. #C', 3)
    ]

    for referral in referrals:
        name: str = referral[0]
        number_of_places: int = referral[1]
        university[name] = parse_referral(join('parser', 'data', f'{name}.csv'), name, number_of_places)

    return university
