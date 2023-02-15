"""
# 1. Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и
# меньшее число. В качестве символа-разделителя 
# используйте пробел.

"""
import random, os
os.system('cls')

N = [random.randint(-10, 10) for _ in range(int(input()))]

print(N)
print(f"{min(N)} {max(N)}")