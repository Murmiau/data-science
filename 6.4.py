class Car:
    def __init__(self, color: str, name: str, is_police: bool):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"Разгон до {speed} км/ч")

    def stop(self):
        self.speed = 0
        print("Стоп")

    def turn(self, direction: str):
        if self.speed > 0:
            print(f"Поворот {direction}")
        else:
            print("Вы стоите, чтобы повернуть, нужно поехать!")

    def show_speed(self):
        print(f"Ваша скорость {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 60:
            print(f"Вы превысили скорость на {self.speed - 60} км/ч")
        else:
            print(f"Ваша скорость {self.speed} км/ч")


class SportCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False


class WorkCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = False

    def show_speed(self):
        if self.speed > 40:
            print(f"Вы превысили скорость на {self.speed - 40} км/ч")
        else:
            print(f"Ваша скорость {self.speed} км/ч")


class PoliceCar(Car):
    def __init__(self, color: str, name: str, is_police: bool):
        super().__init__(color, name, is_police)
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = True


def test_drive(my_car):
    print(f"Начинается тест-драйв автомобиля {my_car.name}, цвет {my_car.color}")
    my_car.show_speed()
    my_car.turn("направо")
    my_car.go(48)
    my_car.show_speed()
    my_car.turn("налево")
    my_car.go(64)
    my_car.show_speed()
    my_car.turn("направо")
    my_car.go(92)
    my_car.show_speed()
    my_car.stop()
    print("Конец тест-драйва! Спасибо за участие!", end="\n\n")


ford = Car("красный", "Ford", False)
test_drive(ford)

polo = TownCar("черный", "Kia", False)
test_drive(polo)

ferrari = SportCar("бирюзовый", "Ferrari", False)
test_drive(ferrari)

opel = WorkCar("синий", "Opel", False)
test_drive(opel)

lada = PoliceCar("белый", "Lada", True)
test_drive(lada)
