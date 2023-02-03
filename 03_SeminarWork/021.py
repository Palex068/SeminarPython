"""
Задача №21. Решение в группах
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
"""

I =  [{"V": "S001"}, {"V": "S002"},
             {"VI": "S001"}, {"VI": "S005"},
             {"VII": " S005 "}, {"V": " S009 "},
             {"VIII": " S007 "}]


result = set([list(i.values())[0].strip() for i in I])
print(I)
print(result)

# num = {k: v ** 3 for k, v in zip("ASDFGHJK", range(1, 11))}
# print(num)