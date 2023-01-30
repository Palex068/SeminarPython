"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.

Input: 5
Output: 6
"""
def user_input():
    while True:
        try:
            number = int(input("Введите число от 1 до 1000: ")) # пока будут волшебные числа, после
            if not number in range(1, 1001):        # поправлю на передаваемый в функцию элемент
                raise ValueError
            return number

        except ValueError:
            print('Вводите только числа от 1 до 1000')

a = user_input()

f0 = 0
f1 = 1
last_f = 1
count = 3
while last_f <  a:
    last_f = f0 + f1
    temp = f1 + last_f
    f0 = f1
    f1 = last_f
    last_f = temp
    count += 1

if last_f == a:
    print(count)
else:
    print("-1")
