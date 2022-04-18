def my_info(**kwargs):
    return '  '.join(kwargs.values())

print(my_info(name=input("Введите, пожалуйста, свое имя: "),
            surname=input("Введите, пожалуйста, свою фамилию: "),
            age = input("Введите, пожалуйста, свой год рождения: "),
            city=input("Введите, пожалуйста, свой город проживания: "),
            email = input("Введите, пожалуйста, свой email: "),
            phone = input("Введите, пожалуйста, свой номер телефона: ")))
