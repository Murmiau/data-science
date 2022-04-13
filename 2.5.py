rating = [1, 4, 4, 9, 6]

while True:
    num = int(input("Введите, пожалуйста, целое положительное число, для завершения програмы напишите 0: "))
    if num > 0:
        rating.append(num)
        rating.sort(reverse=True)
        print(rating)
    if num == 0:
        rating.pop(0)
        break
    else:
        print("Попробуйте еще раз")
