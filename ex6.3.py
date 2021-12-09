class Worker:
    def __init__(self, name, surname, position, bonus, wage):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'bonus': bonus, "profit": wage}

class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"

engineer = Position("Alex", "Ivanov", "ITP", 35000, 80000)
print(engineer.get_full_name())
print(engineer.position)
print(engineer.get_full_profit())
