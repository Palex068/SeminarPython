"""
Задайте число. Составьте список чисел Фибоначчи, в том числе 
для отрицательных индексов.(Доп)

Пример:

для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
[Негафибоначчи]
https://ru.wikipedia.org/w/index.php?go=%D0%9F%D0%B5%D1%80%D0%B5%D0%B9%D1%82%D0%B8&search=%D0%9D%D0%B5%D0%B3%D0%B0%D1%84%D0%B8%D0%B1%D0%BE%D0%BD%D0%B0%D1%87%D1%87%D0%B8&title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F%3A%D0%9F%D0%BE%D0%B8%D1%81%D0%BA&ns0=1
"""

def fibonacci_by_number(n):
    f0, f1, count = 1, 2, 2
    while n >= count:
        if count == n:
            return f1
        f0, f1 = f1, f0 + f1
        count +=1


def fib(n):
    if n in (0, 1):
        return 1
    return fib(n - 1) + fib(n - 2)

def negafib(n):
    if n in (-1, ):
        return 1
    if n in (-2, ):
        return - 1
    return fib(n + 1 ) - fib(n + 2)

# n = int(input())

# print(fibonacci_by_number(n))
       
# print(fib(int(input())))
print(negafib(int(input()) * (- 1)))