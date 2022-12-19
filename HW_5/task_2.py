"""
Реализуйте код игры.
Правила игры: на столе лежит N количество конфет. Играют два игрока, делая ход друг после друга.
Первый ход определяется жеребьёвкой, то есть случаен. За один ход можно забрать не более чем k конфет.
Не брать конфеты НЕЛЬЗЯ. Побеждает тот, кто сделал последний ход, то есть забрал со стола остатки конфет.
Он забирает также все конфеты оппонента.
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего оппонента?

a) Добавьте игру против бота
b) Подумайте, как наделить бота простейшим "интеллектом"
"""


from random import randint
n = int(input('Введите количество конфет '))
k = int(input('Введите количество конфет, которое можно взять за один раз '))
if k < n:
    choise = int(input('Выберите 1 - игрок - игрок. 2 - игрок - компьютер'))
    if choise == 1:
        print('Начинаем игру')
        players = ['1', '2']
        turn = randint(0, 1)
        player = players[turn]  # turn = not turn

        while True:
            print(f'Ходит игрок {player} ')
            d = int(input('Сколько конфет взять со стола:'))
            if d > k:
                print(f'Нельзя брать больше {k}')
                continue
            if d > n:
                print('На столе нет такого количества конфет')
                continue
            n = n - d
            print(f'На столе осталось {n} конфет')
            if n == 0:
                print(f'Выиграл {player}')
                break
            else:
                turn = not turn
                player = players[turn]

    else:
        print('Начинаем игру')
        players = ['1', 'Комп']
        turn = randint(0, 1)
        player = players[turn]  # turn = not turn

        while True:
            print(f'Ходит игрок {player} ')
            if player == '1':
                d = int(input('Сколько конфет взять со стола: '))
            else:
                d = randint(1, k)
                print(f'Компьютер взял {d} конфет')
            if d > k:
                print(f'Нельзя брать больше {k}')
                continue
            if d > n:
                print('На столе нет такого количества конфет')
                continue
            n = n - d
            print(f'На столе осталось {n} конфет')
            if n == 0:
                print(f'Выиграл {player}')
                break
            else:
                turn = not turn
                player = players[turn]
