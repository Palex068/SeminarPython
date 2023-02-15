"""
# 3. Задайте два числа. Напишите программу, которая
# найдёт НОК (наименьшее общее кратное) этих двух чисел.
"""


num1, num2 = ar1, ar2 = int(input()), int(input())

while num1 != 0 and num2 != 0:
    if num1 >= num2:
        num1 %= num2
    else:
        num2 %= num1

result = (ar1 * ar2) / (num1 + num2)

print(int(result))