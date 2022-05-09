class DivisionByZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


def my_class(a, b):
    if b == 0:
        raise DivisionByZeroError(f"{a} / {b} = Ошибка деления на ноль!")
    return a / b


try:
    my_class(12, 0)
except DivisionByZeroError as el:
    print(el)

print(f"Результат деления 15 / 3 = {my_class(15, 3)}")
