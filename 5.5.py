import random
with open("hw8.txt", "w", encoding="UTF-8") as my_file:
    num = ""
    for i in range(10):
        my_file.write(num + str(random.randint(0, 100)))
        num = " "
with open("hw8.txt", "r", encoding="UTF-8") as my_file:
    num_str = my_file.read()
    num_sum = num_str.split(" ")
    print(f"Набор чисел в файле:\n{num_str}")
    print(f"Сумма чисел в файле:\n{sum([int(i) for i in num_sum])}")
    
