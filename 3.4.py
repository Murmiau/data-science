def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "Введите, пожалуйста числа, соответствующие заданию!"
        else:
            xy = x ** y
    except ValueError:
        return "Введите, пожалуйста числа!"
    return xy
print(my_func(x = input("Введите, пожалуйста, действительное положительное число: "),
              y = input("Введите, пожалуйста, целое отрицательное число: ")))