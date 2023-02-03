"""
Задача №19. Решение в группах
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.

Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]
"""

import os, random
os.system('cls')

def user_input(msg):  # безопасный ввод
    while True:
        try:
            # пока будут волшебные числа, после
            number = int(input(f"Введите {msg} (число от 1 до 100): "))
            # поправлю на передаваемый в функцию элемент
            if not number in range(1, 101):
                raise ValueError
            return number

        except ValueError:
            print('Вводите только числа от 1 до 100')

def random_list(n):  # Список случайных чисел, очень не хотелось их вбивать руками))
    N = []
    for _ in range(n):
        N.append(random.randint(-5, 5))
    return N

n = user_input("Количество элементов списка")
N = random_list(n)

print(f"\n{N}\n")

k = user_input("Шаг сдвига")

result = N[(k % n):] + N[:(k % n)]
print(result)

"""
list_nums = [1, 2, 3, 4, 5]
k = 7
print(list_nums)
result = list_nums[(k % len(list_nums)):] + list_nums[:(k % len(list_nums))]
print(result)

list_nums = [1, 2, 3, 4, 5]
k = 7

print(list_nums)

for i in range(k - 1):
    list_nums.insert(0, list_nums.pop(- 1))

print(k, list_nums)
"""