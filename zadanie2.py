st = ''
while st == '':
    st = input('Введите строку: ')
    if st == '':
        print('Вы ввели пустую строку')
print('Ваша строка:', st)

st += ' '
l_words = []
word = ''

for ch in st: # добавление слов в список
    if ch != ' ':
        word += ch
    elif ch == ' ':
        l_words.append(word)
        word = ''

l_a = []
for word in l_words: # поиск нужных слов
    c = 0
    for ch in word:
        if ch == 'a':
            c += 1
    if c >= 2:
        l_a.append(word)
print('Слова, в которых буква "а" входит не менее двух раз:', *l_a)


