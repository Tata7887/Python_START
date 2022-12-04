"""
Задайте список из вещественных чисел, округленных до сотых.
Найдите разницу между максимальным и минимальным значением дробной части элементов.

Ввод: значение типа <list> (либо значения типа <int> – размерность списка)
Вывод: значение типа <float>

Пример:
[1.1, 1.2, 3.1, 5, 10.01]
2.0
"""

import random
size = int(input('Введите размерность '))
str_1 = [round(random.uniform(1.00, 9.00), 2) for i in range(size)]
print(str_1)
str_2 = []
for i in range(size):
    str_2.append(round((str_1[i] % 1), 2))
print(str_2)
print(round(max(str_2) - min(str_2), 2))


