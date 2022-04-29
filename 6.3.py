class Worker:
    def __init__(self, name: str, surname: str, position: str, wage: int, bonus: int):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self.income.values())


Anna = Position("Анна", "Иванова", "Ветеринар", 120000, 35000)
print(Anna.get_full_name())
print(Anna.position)
print(Anna.get_total_income())
