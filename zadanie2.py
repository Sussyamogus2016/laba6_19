st = ''
while st == '':
    st = input('Введите строку: ')
    if st == '':
        print('Вы ввели пустую строку')
print('Ваша строка:', st)
st += ' '
l_words = []
word = ''

for i in range(len(st)):
    if st[i] != ' ':
        word += st[i]
    elif st[i] == ' ':
        l_words.append(word)
        word = ''
print(l_words)

l_a = []
for word in l_words:
    c = 0
    for ch in word:
        if ch == 'a':
            c += 1
    if c >= 2:
        l_a.append(word)
print(l_a)


