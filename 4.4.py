my_num = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11, 18, 1, 3, 10, 6, 15]
new_num = [n for n in my_num if my_num.count(n) == 1]
print("Исходный список:\n", my_num)
print("Элементы исходного списка, не имеющие повторений:\n", new_num)