"""
Напишите программу, удаляющую из текста все слова, в которых присутствуют буквы «а», «б» и «в».

Ввод: значение типа <str>
Вывод: значение типа <str>
"""
str_text = 'На автобус выпал снег'
str_num = []

value = str_text.split()
for i in value:
    if not ("а" in i and "б" in i and "в" in i):
        str_num.append(i)

result = ' '.join(str_num)
print(result)

def del_word_1(str_text):
    return " ".join(filter(lambda x: not("а" in x and "б" in x and "в" in x), str_text.split()))

print(del_word_1(str_text))
