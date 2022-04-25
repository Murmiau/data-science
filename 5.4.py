my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

new_file = ""
with open("hw6.txt", "r", encoding="UTF-8") as my_file:
    new_file = my_file.read()
text_ru = new_file
for en, ru in dictionary.items():
    text_ru = text_ru.replace(en, ru)

with open('task04.tmp', 'w', encoding='UTF-8') as file_ru:
    file_ru.write(text_ru)