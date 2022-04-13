my_list = input("Введите, пожалуйста, любой текст, используя пробелы : ").split()
for n in range(0, len(my_list)-1, 2):
    my_list[n], my_list[n+1] = my_list[n+1], my_list[n]
print(my_list)
