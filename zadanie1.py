st = ''
while st == '':
    st = input('Введите строку: ')
    if st == '':
        print('Вы ввели пустую строку')

print('Ваша строка:', st)
result = ''
in_brackets = False

for ch in st:
    if ch == '(':
        in_brackets = True
        result += ch
    elif ch == ')':
        in_brackets = False
        result += ch
    elif not in_brackets:
        result += ch
print('Измененная строка:', result)