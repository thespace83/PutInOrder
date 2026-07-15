from analyzer import Applicant, Referral


class University:
    def __init__(self, referrals: set[Referral], applicants: set[Applicant]):
        self.referrals: set[Referral] = referrals
        self.applicants: set[Applicant] = applicants
