class Cell(object):
    def __init__(self, size: int):
        if size <= 0:
            raise Exception('Клетка не может иметь меньше одной ячейки')
        self.size = size

    def __add__(self, new):
        return Cell(self.size + new.size)

    def __sub__(self, new):
        result = self.size - new.size
        if result > 0:
            return Cell(result)
        else:
            raise Exception(f"Ошибка! Клеток не может быть меньше 0")

    def __mul__(self, new):
        return Cell(self.size * new.size)

    def __truediv__(self, new):
        return Cell(self.size // new.size)

    def make_order(self, my_size: int) -> str:
        row = ["*" * my_size for _ in range(self.size // my_size)]
        mesh = "*" * (self.size % my_size)
        row.append(mesh)
        return '\n'.join(row)

    def __str__(self):
        return '*' * self.size


if __name__ == "__main__":
    cells_1 = Cell(5)
    cells_2 = Cell(9)
    cells_add = cells_1 + cells_2
    try:
        cells_sub_1 = cells_1 - cells_2
    except Exception as el:
        cells_sub_1 = None
        print(el)
    cells_sub_2 = cells_2 - cells_1
    cells_mul = cells_1 * cells_2
    cells_div = cells_2 / cells_1

    print("1-й ряд клеток:\t", cells_1)
    print("2-й ряд клеток:\t", cells_2)
    print("Cложили ряды:\t", cells_add)
    print("Ряд клеток после вычитания 1-го ряда из 2-го:\t", cells_sub_1)
    print("Ряд клеток после вычитания 2-го ряда из 1-го:\t", cells_sub_2)
    print("Умножили ряды:\t", cells_mul)
    print("Поделили ряды:\t", cells_div)

    cells_make = Cell(37)
    order_37_10 = cells_make.make_order(10)
    print(f"\nВсего ячеек 37 по 10 ячеек в строке:\n{order_37_10}")
