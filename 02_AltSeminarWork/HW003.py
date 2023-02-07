"""
Минимальный делитель
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=3&id_topic=34&id_problem=205

Требуется найти наименьший натуральный делитель 
целого числа N, отличный от 1.

15 -> 3
35 -> 5
"""


def minimum_divisor(n):
    for i in range(2, n + 1):
        if n % i == 0:
            return i


n = int(input("Введите число: "))
print(minimum_divisor(n))


n = int(input("Введите число: "))
flag = True
i = 2
while flag:
    if n % i == 0:
        print(i)
        flag = False
    i += 1
