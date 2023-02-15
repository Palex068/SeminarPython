"""
Задача №43. Решение в группах
Дан список чисел. Посчитайте, сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 
1 2 3 2 3 
Вывод:
2
"""

import random, os
os.system('cls')


N = [random.randint(0, 3) for _ in range(int(input()))]

print(*N)

N_set = set(N)
result = 0
for n in N_set:
    result += (N.count(n) // 2)

print(result)

print(sum(list(N.count(n) // 2 for n in N_set)))