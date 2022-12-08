"""
Задайте целое число N.
Составьте список чисел Фибоначчи размерность 2N + 1 для отрицательной и положительной части (Негафибоначчи).
https://ru.wikipedia.org/wiki/Негафибоначчи

Ввод: значение типа <int>
Вывод: значение типа <list>

Пример:
8
[-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

num = int(input('Введите число N '))
list_fib = [1, 0, 1]
for i in range(num - 1):
    list_fib.append(list_fib[-1] + list_fib[-2])
    list_fib.insert(0, list_fib[1] - list_fib[0])
print(list_fib)


