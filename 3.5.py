def my_summ():
    n = 0
    while True:
        my_num = input("Введите, пожалуйста, числа через пробел. Для выхода нажмите 'e': ").split()
        for num in my_num:
            if num.lower() == "e":
                return n
            else:
                try:
                    n += int(num)
                except ValueError:
                    print("Вы ввели недопустимое значение. Нужно ввести либо числа, "
                          "либо нажать 'e' для выхода!")
        print(f"Сумма чисел = {n}")
print(my_summ())