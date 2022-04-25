import re
new = {}
with open("hw9.txt", "r", encoding="UTF-8") as my_file:
    my_text = my_file.read()
    my_file.seek(0)
    for el in my_file:
        el_items = el.split(": ")
        hours = re.findall(r"\d+", el_items[1])
        new.update({el_items[0]: sum([int(i) for i in hours])})

print(f"Исходный файл:\n{my_text}\n")
print(f"Словарь:\n{new}")