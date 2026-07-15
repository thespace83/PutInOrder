from analyzer import Applicant
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from analyzer import University


def close_admission_campaign(university: 'University') -> dict[str, set[Applicant]]:
    result: dict[str, set[Applicant]] = {}
    for referral in university.referrals:
        result[referral.name] = set()

    print(result)
