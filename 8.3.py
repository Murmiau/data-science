class MyClass(Exception):
    def __init__(self, txt):
        self.txt = txt


def number(string):
    if string.isdigit():
        return string
    else:
        try:
            float(string)
            return string
        except ValueError:
            raise MyClass(f"Ошибка: {string} - это не число")


input_txt = ''
counter = 1
numb_list = []
print("Введите числа по одному, для завершения и получения списка введенных чисел, напишите 'break'.")
while input_txt != 'break':
    try:
        input_txt = input(f"{counter}: ")
        numb_list.append(number(input_txt))
        counter += 1
    except MyClass as el:
        if input_txt != "break":
            print(el.txt)

print(f"Список введенных чисел:\n{numb_list}")
