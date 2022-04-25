with open("homework-5.3.txt", "r") as my_zp:
    sal = []
    poor = []
    my_list = my_zp.read().split("\n")
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
           poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')