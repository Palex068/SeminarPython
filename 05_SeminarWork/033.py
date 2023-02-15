"""
Задача №33. Решение в группах
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.

Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""

# ratings_journal = [int(input()) for _ in range(int(input()))]

# print(ratings_journal)

def max_to_min(list):
    minimum, maximum = min(list), max(list)
    return [minimum if i == maximum else i for i in list]

print(*max_to_min([int(input()) for _ in range(int(input()))]))