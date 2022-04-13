#   mes = int(input("Введите, пожалуйста, месяц в виде его порядкового номера: "))
#   my_dict = {1: "зима", 2: "весна", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень",
#              10: "осень", 11: "осень", 12: "зима"}
#   print(my_dict.get(mes))

mes = int(input("Введите, пожалуйста, месяц в виде его порядкового номера: "))
my_list = ["зима", "весна", "лето", "осень"]
if mes == 12 or mes == 1 or mes == 2:
    print(my_list[0])
elif mes == 3 or mes == 4 or mes == 5:
    print(my_list[1])
elif mes == 6 or mes == 7 or mes == 8:
    print(my_list[2])
elif mes == 9 or mes == 10 or mes == 11:
    print(my_list[3])
else:
    print("Такого месяца не существует!")
