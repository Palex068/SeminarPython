# Задача 1:
# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def user_input():
    while True:
        try:
            number = int(input("Введите трехзначное число: ")) # пока будут волшебные числа, после
            if not number in range(100, 1000):                 # поправлю на передаваемый в функцию элемент
                raise ValueError
            return number

        except ValueError:
            print('Вводите только числа от 100 до 999')

def sum_of_digits(number):
    digits_sum = 0
    digits = ''
    while number > 0:
        digits_sum += int(number%10)
        digits = str(int(number%10)) + digits #TODO Поправить формирование строки
        number //=10
    result = str(digits_sum) + ' (' + digits + ')'
    return result

import os
os.system('cls')

number = user_input()

digits_sum = sum_of_digits(number)

print(f"{number} -> {digits_sum}")

