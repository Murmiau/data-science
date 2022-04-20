new_list = []
my_list = [int(n) for n in input("Введите, пожалуйста, список чисел: ").split()]
for n in range(1, len(my_list)):
    if my_list[n] > my_list[n-1]:
        (new_list.append(my_list[n]))
print("Список чисел, введенных пользователем: ", my_list)
print("Список, элементы которого больше предыдущего: ", new_list)