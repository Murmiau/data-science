with open("hw2.txt", "r", encoding="UTF-8") as my_file:
    text = my_file.readlines()
    print(f"Всего строк: {len(text)}")
    for el, val in enumerate(text):
        words = val.split(" ")
        print(f"Всего слов в строке N{el + 1}: {len(words)}")
