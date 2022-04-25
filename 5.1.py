my_file = open("new_file.txt", "w")
new_str = str
while new_str:
    new_str = input("Введите,пожалуйста, текст, для окончания ввода, используйте пустую строку: \n")
    my_file.writelines(new_str)
    if not str:
        break
my_file.close()
my_file = open("new_file.txt", "r")
print(my_file.readlines())
my_file.close()
