"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.

5 -> 1 0 1 1 0
2
"""
import os, random
os.system('cls')

def user_input(): # безопасный ввод
    while True:
        try:
            number = int(input("Введите число от 1 до 1000: ")) # пока будут волшебные числа, после
            if not number in range(1, 1001):        # поправлю на передаваемый в функцию элемент
                raise ValueError
            return number

        except ValueError:
            print('Вводите только числа от 1 до 1000')

def random_list(n): # Список случайных чисел
    N = []
    for _ in range(n):
        N.append(random.randint(0, 1))
    return N

def print_zero_or_one_counter(N):
    zero_counter = one_counter = 0
    for i in range(len(N)):
        if N[i] == 0:
            zero_counter +=1
        else:
            one_counter +=1
    if zero_counter >= one_counter:
        print(one_counter)
    else:
        print(zero_counter)

n = user_input()
N = random_list(n)
print(N)
print_zero_or_one_counter(N)

#print(*[(s if (s <= n // 2) else (n - s)) for arr in [[int(x) for x in input().split()]] for s in [sum(arr)] for n in [int(len(arr))]])
# это мой ребёнок написал мне на вырост решение в одну строку) буду разбирать, надо соответствовать)