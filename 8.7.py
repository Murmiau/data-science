class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, new):
        a = self.a + new.a
        b = self.b + new.b
        return ComplexNumber(a, b)

    def __mul__(self, new):
        a = (self.a * new.a) - (self.b * new.b)
        b = (self.a * new.b) + (self.b * new.a)
        return ComplexNumber(a, b)

    def __str__(self):
        return f'{self.a} + {self.b}n'


if __name__ == '__main__':
    c1 = ComplexNumber(3, 7)
    c2 = ComplexNumber(5, 9)
    c3 = c1 + c2
    c4 = c1 * c2

    print(f'числа 1 = {c1}')
    print(f'числа 2 = {c2}')
    print(f'числа 1 + числа 2 = {c3}')
    print(f'числа 1 * числа 2 = {c4}')
