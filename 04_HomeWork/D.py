# Задача №1461. Шарики
# В одной компьютерной игре игрок выставляет в линию шарики разных цветов.
# Когда образуется непрерывная цепочка из трех и более шариков одного цвета, 
# она удаляется из линии.
# Все шарики при этом сдвигаются друг к другу, и ситуация может повториться.
# Напишите программу, которая по данной ситуации определяет, сколько шариков 
# будет "уничтожено".
# Естественно, непрерывных цепочек из трех и более одноцветных шаров в начальный момент
# может быть не более одной.
# Входные данные
# A
# Сначала вводится количество шариков в цепочке (не более 1000) и 
# цвета шариков (от 0 до 9, каждому цвету соответствует свое целое число).
# о
# Ө
# Выходные данные
# Требуется вывести количество шариков, которое будет "уничтожено".
# Примеры
# входные данные
# 5 1 3 3 3 2
# выходные данные
# 3


import random

N = [random.randint(0, 2) for _ in range(int(input("Введите количество шариков: ")))]
# N = [5, 1, 3, 3, 3, 2]

# print(*N)

temp_list = list()
index = 0
while index < (len(N) - 2):
    if N[index] == N[index + 1] and N[index] == N[index + 2]:
        index += 3
    else:
        temp_list.append(N[index])
        index += 1
# print(*temp_list)

print((len(N) - len(temp_list)) // 3)