import re


class Date:
    max_days_in_month_1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    max_days_in_month_2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, my_date):
        match_result = re.match(r'^\d\d-\d\d-\d\d\d\d$', my_date)
        if match_result is None:
            raise Exception(f"{my_date} - Некорректный формат даты, используйте формат: dd-mm-yyyy")
        self.date_string = my_date
        self.day, self.month, self.year = map(int, my_date.split('-'))

    @classmethod
    def extract(cls, my_date):
        date = cls(my_date)
        return [date.day, date.month, date.year]

    @staticmethod
    def validate(my_date):
        date = Date(my_date)
        is_not_zero = date.day > 0 and date.month > 0 and date.year > 0
        if date.year % 4 == 0 and date.year % 100 != 0 or date.year % 400 == 0:
            boundaries = date.month <= 12 and date.day <= date.max_days_in_month_2[date.month - 1]
        else:
            boundaries = date.month <= 12 and date.day <= date.max_days_in_month_1[date.month - 1]
        return is_not_zero and boundaries


if __name__ == '__main__':
    my_real_date = '04-05-2022'
    my_not_date = '32-05-2022'
    my_incorrect_date = 'gewh'

    real_date = Date(my_real_date)
    print(f"{real_date.extract(my_real_date)} - Введенные числа")

    not_date = Date(my_not_date)
    print(f"{real_date.extract(my_not_date)} - Введенные числа")

    try:
        incorrect_date = Date(my_incorrect_date)
    except Exception as el:
        print(el)

    if Date.validate(my_real_date):
        print(f"{my_real_date} - Дата")
    else:
        print(f"{my_real_date} - Такой даты не существует")

    if Date.validate(my_not_date):
        print(f"{my_not_date} - Дата")
    else:
        print(f"{my_not_date} - Такой даты не существует")
