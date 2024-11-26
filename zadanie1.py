st = ''
while st == '':
    st = input('Введите строку: ')
    if st == '':
        print('Вы ввели пустую строку')

result = ''
in_brackets = False

for ch in st:
    if ch == '(':
        in_brackets = True
        result += ch  # сохраняем открытую скобку
    elif ch == ')':
        in_brackets = False
        result += ch  # сохраняем закрытую скобку
    elif not in_brackets:
        result += ch  # сохраняем символ, если не внутри скобок
print(result)
