# 2. Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.

# Примеры:

# - 1, 4, 8, 7, 5 -> 8
# - 78, 55, 36, 90, 2 -> 90

numbers = []
n = 5
for i in range(n):
    numbers.append(int(input()))
result = max(numbers)
print(result)