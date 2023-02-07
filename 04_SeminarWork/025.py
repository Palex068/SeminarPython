"""
Задача №25. Решение в группах
Напишите программу, которая принимает на вход
строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к
символам с помощью постфикса формата _n.

Input: a a a b c a a d c d d

Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

Для решения данной задачи используйте функцию
.split()
"""
"""
string = input().split()

for i in range(len(string)):
    count = 1
    for j in range(i + 1, len(string)):
        if string[i] == string[j]:
            string[j] += "_" + str(count)
            count += 1
    

print(*string)
"""
string = input().split()

D = {}.fromkeys(string, 0)
# print(D)

for i in string:
    print(f"{i}_{D[i]}" if D[i] else i, end=" ")
    D[i] += 1