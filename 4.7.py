from math import factorial
n = int(input("Введите, пожалуйста, целое число до которого будет вычислен ряд факториалов: "))
def new_factorial(n):
    for i in range(n+1):
        print(i, end='! = ')
        yield factorial(i)

print("Результаты вычисления факториала чисел: ")
for el in new_factorial(n):
    print(el)