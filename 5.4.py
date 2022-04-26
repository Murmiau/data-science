my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

new_file = ""
with open("hw6.txt", "r", encoding="UTF-8") as my_file:
    print(my_file.read())
with open("hw6.txt", "r", encoding="UTF-8") as my_file:
    new_file = my_file.read()
text_rus = new_file
for en, ru in my_dict.items():
    text_rus = text_rus.replace(en, ru)

with open("hw7.txt", "w", encoding="UTF-8") as file_rus:
    file_rus.write(text_rus)
with open("hw7.txt", "r", encoding="UTF-8") as file_rus:
    print(file_rus.read())
