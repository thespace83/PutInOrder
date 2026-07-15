from analyzer import Applicant
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from analyzer import University, Referral


def get_minimal_points(university: 'University', referral: 'Referral') -> int:
    if referral.number_of_places > len(university.result[referral.name]):
        return 0

    minimum_points: int = 999
    for applicant in university.result[referral.name]:
        if applicant.amount_of_points < minimum_points:
            minimum_points = applicant.amount_of_points

    return minimum_points


def get_undocumented_applicant(university: 'University') -> Applicant | None:
    for applicant in university.applicants:
        documented: bool = False
        for referral in university.result.keys():
            if university.result[referral].__contains__(applicant):
                documented = True
                break
        if not documented:
            return applicant
    return None


def remove_under(university: 'University', referral: 'Referral'):
    points = get_minimal_points(university, referral)
    candidates: set[Applicant] = set()
    for applicant in university.result[referral.name]:
        print(applicant.amount_of_points, points)
        if applicant.amount_of_points <= points:
            candidates.add(applicant)

    lowes_priority_applicant: Applicant = next(iter(candidates))
    for candidate in candidates:
        if candidate.priorities[referral.name] > lowes_priority_applicant.priorities[referral.name]:
            lowes_priority_applicant = candidate
    university.result[referral.name].remove(lowes_priority_applicant)


def enroll(university: 'University', applicant: Applicant):
    for priority in range(len(applicant.priorities)):
        referral = university.get_referral_by_name(applicant.get_list_of_priorities()[priority])
        if referral is None:
            raise 'Referral is None'
        minimal_points = get_minimal_points(university, referral)
        if minimal_points < applicant.amount_of_points:
            university.result[referral.name].add(applicant)
            if len(university.result[referral.name]) > referral.number_of_places:
                remove_under(university, referral)
            return


def close_admission_campaign(university: 'University') -> 'University':
    for referral in university.referrals:
        university.result[referral.name] = set()

    undocumented_applicant = get_undocumented_applicant(university)
    while undocumented_applicant is not None:
        # ---
        for name in university.result.keys():
            print(f'{name}: ', end='')
            for a in university.result[name]:
                print(a.uuid, end=', ')
            print()
        print()
        # ---
        enroll(university, undocumented_applicant)
        undocumented_applicant = get_undocumented_applicant(university)

    return university
