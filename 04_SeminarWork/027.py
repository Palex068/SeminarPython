"""
Задача №27. Решение в группах
Пользователь вводит текст(строка). Словом считается
последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом
пробелов. Определите, сколько различных слов
содержится в этом тексте.

Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

Output: 13

"""

string = input()
print(string)

punctuation_marks = [".",",", ";", ":", "?", "!"]

for i in punctuation_marks:
    string = string.replace(i, " ")

print(string)

split_lower_string = string.lower().split()

print(split_lower_string)

set_string = set(split_lower_string)

print(set_string)

print(len(set_string))


string = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
string = set(string.lower().split())
print(len(string))
