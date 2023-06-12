a = float(input("Введите число 1 = "))
b = input("Введите выражение 1 = ")
c = float(input("Введите число 2 = "))
d = input("Введите выраженте 2 = ")
e = float(input("Введите число 3 = "))
tot = 0
if (c == 0 and b == '/') or (e == 0 and d == '/'):
    print('ERROR')
else:
    if b == '-':
        tot = a - c
    elif b == '+':
        tot = a + c
    elif b == '*':
        tot = a * c
    elif b == '/':
        tot = a / c
    if d == '-':
        print(tot - e)
    elif d == '+':
        print(tot + e)
    elif b == '+' and d == '*':
        print(a + c * e)
    elif b == '-' and d == '*':
        print(a - c * e)
    elif b == '+' and d == '/':
        print(a + c / e)
    elif b == '-' and d == '/':
        print(a - b / e)

