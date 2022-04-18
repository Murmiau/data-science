num1 = int(input("Введите, пожалуйста, число, которое хотите поделить: "))
num2 = int(input("Введите, пожалуйста, число, на которое хотите поделить: "))
def my_func(num1, num2):
    return num1 // num2
try:
    print(my_func(num1, num2))
except ZeroDivisionError:
    print("На ноль делить нельзя")

#while True:
#    num1 = int(input("Введите, пожалуйста, число, которое хотите поделить: "))
#    num2 = int(input("Введите, пожалуйста, число, на которое хотите поделить: "))
#    if num2 == 0:
#        print("Выберите, пожалуйста, другое число, на ноль мы не делим!")
#    else:
#       def my_del(num1, num2):
#            return num1 // num2
#        print(my_del(num1, num2))
#        break
