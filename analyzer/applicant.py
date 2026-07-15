class Applicant:
    def __init__(self, uuid: int, priorities: dict[str, int], amount_of_points: int):
        self.uuid: int = uuid
        self.priorities: dict[str, int] = priorities
        self.amount_of_points: int = amount_of_points

    def get_list_of_priorities(self) -> list[str]:
        priorities: list[str] = [''] * len(self.priorities.keys())
        for name in self.priorities.keys():
            priorities[self.priorities[name] - 1] = name
        return priorities

    def __eq__(self, other):
        return self.uuid == other.uuid

    def __hash__(self):
        return self.uuid.__hash__()

    def __str__(self):
        return f'{self.uuid} // {self.amount_of_points} // {self.priorities}'
