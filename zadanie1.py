st = ''
while st == '':
    st = input('Введите строку: ')
    if st == '':
        print('Вы ввели пустую строку')

for i in range(len(st)):
    count_open = count_close = 0
    if st[i] == '(':
        count_open += 1
        ind_open = i
    if st[i] == ')':
        count_close += 1
        ind_close = i
    if count_open == count_close == 1:
        st = st[0:ind_open]
