from analyzer import Applicant, Referral, University
from os.path import join
from os import listdir
import json


class LocalApplicant:
    def __init__(self, uuid: int, amount_of_points: int, priority: int, ):
        self.uuid: int = uuid
        self.amount_of_points: int = amount_of_points
        self.priority: int = priority


def parse_local_applicant(row: str) -> LocalApplicant | None:
    data: list[str] = row[:-1].split(';')
    consent_submitted: bool = False if data[3] == '"—"' else True
    if not consent_submitted:
        return None

    uuid = int(data[1])
    amount_of_points = int(data[4])
    priority: int = int(data[2])

    return LocalApplicant(uuid, amount_of_points, priority)


def parse_local_applicants(path: str) -> set[LocalApplicant]:
    file = open(path, 'rb')
    file.readline()

    local_applicants: set[LocalApplicant] = set()
    for row in file.readlines():
        local_applicant = parse_local_applicant(row.decode('utf-8'))
        if local_applicant:
            local_applicants.add(local_applicant)

    return local_applicants


def add_applicant(local_applicant: LocalApplicant, referral: Referral, applicants: set[Applicant]):
    for applicant in applicants:
        if applicant.uuid == local_applicant.uuid:
            applicant.priorities[referral.name] = local_applicant.priority

    applicants.add(Applicant(local_applicant.uuid,
                             {referral.name: local_applicant.priority},
                             local_applicant.amount_of_points))


def get_sources() -> set[Referral]:
    data = json.loads(open('data.json', 'r').read())

    referrals: set[Referral] = set()
    for file in listdir(join('data')):
        name = file.split('.')[0]
        referrals.add(Referral(name + f'.{file.split('.')[1]}', data[name]))

    return referrals


def parse_university() -> University:
    referrals: set[Referral] = get_sources()
    applicants: set[Applicant] = set()

    for referral in referrals:
        for local_applicant in parse_local_applicants(join('data', f'{referral.name}.csv')):
            add_applicant(local_applicant, referral, applicants)

    return University(referrals, applicants)
