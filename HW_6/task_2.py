"""
Задайте список случайных чисел. Выведите:
а) список чисел, которые не повторяются в заданном списке,
б) список повторяемых чисел,
в) список без повторений

Ввод: значение типа <list>
Вывод: три объекта типа <list>

Пример:
[1, 2, 3, 5, 1, 5, 3, 10]
[2, 10]
[1, 3, 5]
[1, 2, 5, 3, 10]
"""
import random
size = int(input('Введите размерность '))
str_1 = [random.randint(1, 9) for i in range(size)]
str_2 = []
str_3 = []
str_4 = []
print(str_1)

for i in str_1:
    if str_1.count(i) == 1:
        str_2.append(i)
    elif i not in str_3:
        str_3.append(i)
    if i not in str_4:
        str_4.append(i)
    i += 1

print(str_2)
print(str_3)
print(str_4)
