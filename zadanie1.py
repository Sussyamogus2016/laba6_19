st = ''
while st == '':
    st = input('Введите строку: ')
    if st == '':
        print('Вы ввели пустую строку')

for i in range(len(st)):
    if st[i] == '(':
        for j in range(i, len(st)):
            if st[j] == ')':
                for k in range(0, )


