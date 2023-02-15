"""
Задайте список из вещественных чисел. 
Напишите программу, которая найдёт разницу 
между максимальным и минимальным значением 
дробной части элементов.

Пример:

- [1.1, 1.2, 3.1, 5, 10.01] => 0.19
"""
import random, os
os.system('cls')


N = [round(random.uniform(0, 6), 2) for _ in range(int(input()))]
print(N)
result = list(round((int((i - int(i)) * 100)) / 100, 2) for i in N)
print(result)
print(round((max(result) - min(result)), 2))