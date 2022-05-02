class Clothe:
    def __init__(self, name: str):
        self.name = name

    def fabric(self):
        pass


class Coat(Clothe):
    def __init__(self, name: str, size: int):
        self.size = size
        super().__init__(name)

    @property
    def fabric(self):
        return round(self.size / 6.5 + 0.5, 1)


class Suit(Clothe):
    def __init__(self, name: str, height: float):
        self.height = height
        super().__init__(name)

    @property
    def fabric(self):
        return round(2 * self.height + 0.3, 1)


if __name__ == "__main__":
    my_coat = Coat("Черное пальто", 52)
    my_suit = Suit("Классический костюм", 1.76)
    print("Расход ткани на пошив черного пальто:", my_coat.fabric, "метров")
    print("Расход ткани на пошив классического костюма:", my_suit.fabric, "метров")
