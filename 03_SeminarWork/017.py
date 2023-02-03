"""
Задача №17. Решение в группах
Дан список чисел. Определите, сколько в нем
встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
"""

import os, random
os.system('cls')

def user_input():  # безопасный ввод
    while True:
        try:
            # пока будут волшебные числа, после
            number = int(input("Введите число от 1 до 1000: "))
            # поправлю на передаваемый в функцию элемент
            if not number in range(1, 1001):
                raise ValueError
            return number

        except ValueError:
            print('Вводите только числа от 1 до 1000')

def random_list(n):  # Список случайных чисел, очень не хотелось их вбивать руками))
    N = []
    for _ in range(n):
        N.append(random.randint(-5, 5))
    return N

n = user_input()
N = random_list(n)

print(N)

result = set()

for i in N:
    result.add(i)

print(sorted(result))
print(len(result))

print(len(set(i for i in [random.randint(-5, 5) for _ in range(int(input("Введите число ")))])))
