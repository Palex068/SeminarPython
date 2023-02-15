"""
Задача №45. Решение в группах
Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 10 ** 5
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).

Ввод:
300

Вывод:
220 284
"""

"""
def pair(value):
    # Получаем корень числа, отбрасываем дробную часть
    sq_num = int(value ** 0.5)

    # Выставляем начальное значение в переменной
    # Если переменная sq_num возведённая в квадрат
    # не равна полученному числу, прибавляем 0.
    # Иначе прибавляем это число, т.к. оно тоже множитель
    res = 1 + (0 if sq_num ** 2 != value else sq_num)

    # Цикл от 2 др корня числа
    for i in range(2, sq_num):

        # Если полученное число делиться на i без остатка
        if value % i == 0:
            # Складываем в переменную значение i
            # и второй делитель, например
            # value = 10, i = 2, второй делитель 5
            res += i + value // i
    return res


for j in range(10, 300):
    # Первое число, это сумма множителей j
    sum1 = pair(j)

    # Второе число, это сумма множителей sum1
    sum2 = pair(sum1)

    # Если второе число равно j и первое число меньше второго
    # Второе условие защита от дубликатов,
    # записанных наоборот
    if sum2 == j and sum1 < sum2:
        print(j, sum1)
"""

# решето Эратосфена


def is_prime_list(number):
    prime_list = [True for _ in range(2, number + 3)]
    prime_list[0], prime_list[1] = False, False
    for i in range(2, int(len(prime_list) ** 0.5) + 1):
        if(prime_list[i]):
            for j in range(i * i, len(prime_list), i):
                prime_list[j] = False
    return prime_list


def list_of_divisors(number):
    list_of_divisors = list()
    if prime_list[number]:
        list_of_divisors.append(number)
        return list_of_divisors
    n = number
    for d in range(2, int(n ** 0.5 + 1)):
        if prime_list[d]:
            while n % d == 0:
                list_of_divisors.append(d)
                n //= d
    if prime_list[n]:
        list_of_divisors.append(n)
    return list_of_divisors



number = int(input())
prime_list = is_prime_list(number)

# print(*list(i for i in range(len(prime_list)) if prime_list[i]))
result = list_of_divisors(number)
print(*result)

