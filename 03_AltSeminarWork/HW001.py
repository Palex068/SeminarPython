"""
Задайте список из нескольких чисел. Напишите программу, которая найдёт 
сумму элементов списка, стоящих на нечётной позиции.

Пример:

[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9,
ответ: 12

"""

import random, os
os.system('cls')


N = [random.randint(0, 10) for _ in range(int(input()))]
print(*N)
result =list(N[i] for i in range(len(N)) if i % 2 != 0)
print(*result, sep= " + ", end= " = " + str(sum(result)))