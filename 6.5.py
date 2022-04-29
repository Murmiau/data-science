class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"Запуск отрисовки {self.title}")


class Pen(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} ручкой")


class Pencil(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} карандашем")


class Handle(Stationery):
    def draw(self):
        print(f"Запуск отрисовки {self.title} маркером")


stationery = Stationery("акварельными красками")
stationery.draw()

pen = Pen("синей")
pen.draw()

pencil = Pencil("цветным")
pencil.draw()

handle = Handle("водостойким")
handle.draw()
