import json
rep = []
with open("hw10.txt", "r", encoding="UTF-8") as my_file:
    my_text = my_file.read()
    my_file.seek(0)
    prof = {}
    prof_summ = 0
    n = 0
    for el in my_file:
        item = el.split(" ")
        profit = int(item[2]) - int(item[3])
        if profit > 0:
            prof.update({item[0]: profit})
            prof_summ += profit
            n += 1
        else:
            prof.update({item[0]: profit})
            n += 0
    rep.append(prof)
    rep.append({"Полученная прибыль": (prof_summ / n)})
with open("hw11.txt", "w", encoding="UTF-8") as json_file:
    json.dump(rep, json_file, ensure_ascii=False)
json_report = json.dumps(rep, ensure_ascii=False)

print(f"Исходный файл:\n{my_text}\n")
print(f"Список фирм с прибылью/убытком:\n{rep}\n")
print(f"json-объект:\n{json_report}")
