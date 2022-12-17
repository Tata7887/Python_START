"""
Даны файлы, в каждом из которых находится запись многочлена.
Найти сумму многочленов из файлов, ввести в консоль и записать в файл.
Входными данными для этой задачи являются выходные данные их предыдущей.

Ввод: значения типа <str>, полученные из файлов.
Вывод: значение типа <str>, файл с одной строкой.

Примеры:
9x^5+7x^4+7x^3+9x^2+6x+17=0
3x^2+2x+1=0
9x^5+7x^4+7x^3+12x^2+8x+18=0
"""
from os import path, chdir, listdir
from sympy.abc import x
from sympy import *


def sum_poly(*args):
    res = []
    for arg in args:
        if arg != "":

            #print(arg)

            s = arg.replace('x', ' * x').replace('x^', 'x ** ').replace(' = 0', '')
            s = s.replace(' +  *', ' + 1 *') #
            if s[0] == ' ':
                s = '1' + s
            #print(s)
            res.append(collect(s, x))
    return str(sum(res)).replace('*x', 'x').replace('**', '^') + ' = 0'


if __name__ == '__main__':
    if path.isdir("polynom"):
        chdir("polynom")
    else:
        print("Каталог с файлом отсутствует")
        exit()

    res_polynom = ""
    for file_name in listdir():
        if "polynom" in file_name:
            with open(file_name, 'r') as file:
                str_polynom = file.read()
                print(f"{str_polynom}  из файла {file.name}")
                res_polynom = sum_poly(res_polynom, str_polynom)
    print(res_polynom)
