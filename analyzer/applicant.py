class Applicant:
    def __init__(self, uuid: int, priorities: dict[str, int], amount_of_points: int):
        self.uuid: int = uuid
        self.priorities: dict[str, int] = priorities
        self.amount_of_points: int = amount_of_points
        self.dropped_out: bool = False

    def get_list_of_priorities(self) -> list[str]:
        priorities: list[str] = [''] * self.get_lowest_priority()
        for name in self.priorities.keys():
            priorities[self.priorities[name] - 1] = name
        return priorities

    def get_lowest_priority(self) -> int:
        lowest_prior: int = 0
        for name in self.priorities.keys():
            if self.priorities[name] > lowest_prior:
                lowest_prior = self.priorities[name]
        return lowest_prior

    def __eq__(self, other):
        return self.uuid == other.uuid

    def __hash__(self):
        return self.uuid.__hash__()

    def __str__(self):
        return f'{self.uuid} // {self.amount_of_points} // {self.priorities} // {self.dropped_out}'
