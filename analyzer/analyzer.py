from analyzer import Applicant

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


def close_admission_campaign(university: dict[str, set[Applicant]]) -> dict[str, set[Applicant]]:
    applicants = get_applicants(university)

