from sys import argv

script_name, hour_prod, rate_hour, bon = argv

print("Имя скрипта: ", script_name)
print("Скрипт для расчета заработной платы сотрудников: ")
print("Выработка в часах: ", hour_prod)
print("Ставка в час: ", rate_hour)
print("Премия: ", bon)
print("Заработная плата сотрудника: ", (float(hour_prod) * float(rate_hour)) + float(bon))