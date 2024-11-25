import random
def abs(n):
    if n < 0:
        return n*(-1)
    return n

while True:
    try:
        n = int(input('Введите размер списка: '))
        break
    except Exception:
        print('Ошибка!')

l = [random.randint(-100,100) for i in range(n)]
print('Ваш список:', l)

mx = l[0]
s = 0
for i in range(len(l)):
    if abs(l[i]) > abs(mx):
        mx = l[i]
print('Максимальный по модулю элемент списка: ', mx)

index = s = 0
for i in range(n):
    if l[i] > 0:
        index = i
        break
for i in range(index+1, n):
    s += l[i]

if s == 0:
    print('Положительные элементы отсутствуют')
else:
    print('Сумма элементов, расположенных после первого положительного элемента',l[index], ':', s)
