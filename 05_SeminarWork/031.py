"""
Задача №31. Решение в группах
Последовательностью Фибоначчи называется
последовательность чисел a0
, a1
, ..., an
, ..., где
a0
 = 0, a1
 = 1, ak
 = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 21
Задание необходимо решать через рекурсию
      1  2  3  4  5   6   7   8   9  10   11   12   13   14   15
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
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


n = int(input())

print(fibonacci_by_number(n))
       
print(fib(int(input())))
