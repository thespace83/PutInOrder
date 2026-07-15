from analyzer import Applicant


class Referral:
    def __init__(self, name: str, number_of_places: int):
        self.name: str = name
        self.number_of_places: int = number_of_places
        self.applicants: set[Applicant] = set()

    def __str__(self):
        applicants: str = ''
        for a in self.applicants:
            applicants += '\n   ' + a.__str__()
        return f'{self.name} // {self.number_of_places}{applicants}'
