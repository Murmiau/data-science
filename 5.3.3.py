my_f = open("homework-5.3.txt", "r")
content = my_f.read()
sal = []
poor = []
content.split("\n")
for i in content:
    i = i.split()
    if int(i[1]) < 20000:
        poor.append(i[0])
        sal.append(i[1])
    print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')
my_f.close()