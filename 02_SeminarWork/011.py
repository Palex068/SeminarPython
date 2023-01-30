"""
Задача №11. Решение в группах
Дано натуральное число A > 1. Определите, каким по
счету числом Фибоначчи оно является, то есть
выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.

Input: 5
Output: 6
"""

# 1  2  3  4  5  6  7   8   9  10  11
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,

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

f0, f1, count = 0, 1, 2

while f1 <=  a:
    if f1 == a:
        print(count)
        break
    f0, f1 = f1 ,f0 + f1
    count += 1
else:
    print("-1")
