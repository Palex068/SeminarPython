"""
https://acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=3&id_topic=33&id_problem=197
Сумма

Требуется посчитать сумму целых чисел, 
расположенных между числами 1 и N включительно.

Пример

5 -> 15
"""

n = int(input("Введите число: "))

result = 0

for i in range(1, n + 1):
    result +=i
print(result)

print(sum(i for i in range(1, (int(input("Введите число: ")) + 1))))

n = int(input("Введите число: "))
print(int(((n +1) / 2) * n))


# Рекурсия


def Count_num(count):
    if count == 0:
        return 0
    return Count_num(count - 1) + count


count = int(input('Введите: '))
print(Count_num(count))