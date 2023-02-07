"""
Второй максимум

Задана последовательность натуральных чисел, завершающаяся числом 0. 
Требуется определить значение второго по величине элемента в этой 
последовательности, то есть элемента, который будет наибольшим, 
если из последовательности удалить наибольший элемент.

"""
n = int(input())
first_max = n
second_max = n - 1

while n != 0:
    n = int(input())
    if n > first_max:
        second_max = first_max
        first_max = n
    elif n > second_max:
        second_max = n
print(second_max)
