"""
Последовательностью Фибоначчи называется последовательность чисел 
a0, a1, ..., an, ..., где

a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).

Требуется найти N-е число Фибоначчи.
"""


def fibonacci_by_number(n):
    f0, f1, count = 0, 1, 2
    while n >= count:
        if count == n:
            return f1
        f0, f1 = f1, f0 + f1
        count +=1


n = int(input())
result = fibonacci_by_number(n)
print(result)