from analyzer import Applicant, Referral


class University:
    def __init__(self, referrals: set[Referral], applicants: set[Applicant]):
        self.referrals: set[Referral] = referrals
        self.applicants: set[Applicant] = applicants
        self.result: dict[str, set[Applicant]] = {}

    def get_referral_by_name(self, name: str) -> Referral | None:
        for referral in self.referrals:
            if referral.name == name:
                return referral

        return None
