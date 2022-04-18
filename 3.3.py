def my_summ(num1, num2, num3):
    my_num = [num1, num2, num3]
    try:
        my_num.remove(min(my_num))
        return sum(my_num)
    except TypeError:
        return "Пожалуйста, введите числа."
print(my_summ(num1 = int(input("Введите, пожалуйста, первое число: ")),
              num2 = int(input("Введите, пожалуйста, второе число: ")),
              num3 = int(input("Введите, пожалуйста, второе число: "))))