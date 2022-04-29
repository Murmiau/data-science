class Road:
    def __init__(self, length: int, width: int):
        self.my_length = length
        self.my_width = width

    def get_mass(self, mass_1m2: int, thickness: int):

        mass = self.my_length * self.my_width * mass_1m2 * thickness // 1000
        return mass


my_road = Road(5000, 20)
assert my_road.get_mass(25, 5) == 12500
print("Все работает корректно!")
