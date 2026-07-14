class Applicant:
    def __init__(self, uuid: int, priority: int, consent_submitted: bool, amount_of_points: int):
        self.uuid: int = uuid
        self.priority: int = priority
        self.consent_submitted: bool = consent_submitted
        self.amount_of_points: int = amount_of_points

    def __eq__(self, other):
        return self.uuid == other.uuid

    def __hash__(self):
        return self.uuid.__hash__()
