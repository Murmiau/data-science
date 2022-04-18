def int_func(text):
    lat = "zxcvbnmasdfghjklqwertyuiop"
    if text.islower():
        return text.title() if not set(text).difference(lat) else print\
            ("Попробуйте еще раз ввести фразу на латинице в нижнем регистре!")
    else:
        print("Введите, пожалуйста, фразу на латинице в нижнем регистре!")

text = input("Введите, пожалуйста, фразу, целиком состоящую "
                      "из букв в нижнем регистре на латинице: ").split()
for i in text:
    res = int_func(i)
    if res:
        print(res)
