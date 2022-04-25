with open("hw5.txt", "r", encoding="UTF-8") as my_zp:
    num = []
    fil = []
    my_list = my_zp.read().split("\n")
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           fil.append(i[0])
        num.append(i[1])
print(f"Оклад меньше 20000: {fil}, средний оклад у специалистов: {sum(map(int, num)) / len(num)}")
