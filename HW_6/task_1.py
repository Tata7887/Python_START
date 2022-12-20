"""
Напишите программу вычисления арифметического выражения заданного строкой.
Используйте операции +,-,/,*. приоритет операций стандартный.
По возможности реализуйте использования скобок, меняющих приоритет операций.

Ввод: значение типа <str>
Вывод: значение числового типа данных
"""
def calc(a, b, symbol):
    a, b = float(a), float(b)
    match symbol:
        case '+':
            return a + b
        case '-':
            return a - b
        case '/':
            return a / b
        case '*':
            return a * b


def parse_exp(exp: str):
    if len(exp) == 1:
        return float(exp)

    if not exp:
        return 0

    symbols = '-+*/'

    for symbol in symbols:
        if symbol in exp:
            a, b = exp.split(symbol, 1
                             )
            return calc(parse_exp(a), parse_exp(b), symbol)

def start(exp: str):
    return parse_exp(''.join(exp.split()))

if __name__ == '__main__':
    # exp = '-4 / 2 * 3'
    exp = '4 / 2 * 3'
    # exp = '-2 * 3'
    print(start(exp))
