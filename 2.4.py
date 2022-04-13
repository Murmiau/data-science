my_list = input("Введите, пожалуйста, любой текст, используя пробелы: ").split()
for ind, el in enumerate(my_list, 1):
    print(ind, el[0:10])
