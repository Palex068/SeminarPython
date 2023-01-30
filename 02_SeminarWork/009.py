"""
Задача №9. 
Решение в группах

По данному целому неотрицательному n вычислите
значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
чисел от 1 до N) 0! = 1 Решить задачу используя цикл
while

Input: 5
Output: 120
"""

def user_input():
    while True:
        try:
            number = int(input("Введите число от 1 до 100: ")) # пока будут волшебные числа, после
            if not number in range(1, 101):        # поправлю на передаваемый в функцию элемент
                raise ValueError
            return number

        except ValueError:
            print('Вводите только числа от 1 до 100')

def factorial(number):
    factorial = 1
    while number > 0:
        factorial *= number
        number -= 1
    return factorial


n = user_input()
f = factorial(n)

print(f)