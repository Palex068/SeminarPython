"""
Напишите программу, которая будет преобразовывать десятичное число в двоичное.

Пример:

- 45 -> 101101
- 3 -> 11
- 2 -> 10
"""
number = int(input())
base = 2
base_digits = list()
n = number
while n != 1:
    base_digits.append(n % base)
    n //= base
base_digits.append(1)
# print(base_digits)
result = list(reversed(base_digits))
print(*result, sep="")
print(bin(number)[2:])
