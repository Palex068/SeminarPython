"""
Напишите программу, которая найдёт 
произведение пар чисел списка. 
Парой считаем первый и последний элемент, 
второй и предпоследний и т.д.

Пример:

- [2, 3, 4, 5, 6] => [12, 15, 16];
- [2, 3, 5, 6] => [12, 15]
"""

import random, os
os.system('cls')


N = [random.randint(0, 10) for _ in range(int(input()))]
print(N)
result = list(N[i] * N[- (i + 1)] for i in range(len(N) // 2 if len(N) % 2 == 0 else len(N) // 2 + 1 ))
print(result)
