# Чтобы не писать так :
a = int(input())
if a >= 90:
    print(5)
else:
    if a >= 80:
        print(4)
    else:
        if a >= 50:
            print(3)
        else:
            if a >= 30:
                print(2)
            else:
                print(1)
# Проще написать так:
a = int(input())
if a >= 90:
    print(5)
elif a >= 80:
    print(4)
elif a >= 50:
    print(3)
elif a >= 20:
    print(2)
else:
    print(1)

# Задача нужно чтобы программа вывел сколько чисел равно 3 2 или 0
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b:
    print(2)
elif b == c:
    print(2)
elif a == c:
    print(2)
else:
    print(0)

# Так же можно использовать операторы or and
a, b, c = int(input()), int(input()), int(input())
if a == b == c:
    print(3)
elif a == b or b == c or a == c:
    print(2)
else:
    print(0)

a = 90
if a == 90:
    print(4)
else:
    print(1)
if a > 0:
    print(4)
else:
    print(1)
# Ответ будет 4 4 потому что это отдельная конструкция второй if
# ПРимер со stpepik
angle = int(input())
if angle % 90 == 0:
    if angle == 0:
        print('Нулевой')
    elif angle == 90:
        print('Прямой')
    elif angle == 180:
        print('Развёрнутый')
else:
    if 0 < angle < 90:
        print('Острый')
    elif 90 < angle < 180:
        print('Тупой')
    elif 180 < angle < 270:
        print('Выпуклый')
    else:
        print('Ни острый, ни тупой, ни выпуклый')

# Мой код если стороны треугольника равны он равносторонний, 2 стороны равны равнобедренный, все разнные разносторонний
a = int(input())
b = int(input())
n = int(input())
if a == b == n:
    print('Равносторонний')
elif a == b or a == n or b == n:
    print('Равнобедренный')
else:
    print('Разносторонний')

# Калькулятор с учетом деления на 0, было тяжело ...
a = int(input())  # Число
b = int(input())  # Исчесляемое
c = input()  # Знак
if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif b == 0 and c == '/':
    print('На ноль делить нельзя!')
elif c == '/':
    print(a / b)
    
# КАзино
a = int(input())

if a == 0:
    print('зеленый')
elif 1 <= a <= 10:
    if a % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 11 <= a <= 18:
    if a % 2 == 0:
        print('красный')
    else:
        print('черный')
elif 19 <= a <= 28:
    if a % 2 == 0:
        print('черный')
    else:
        print('красный')
elif 29 <= a <= 36:
    if a % 2 == 0:
        print('красный')
    else:
        print('черный')
else:
    print('ошибка ввода')
# Я делал a <= 11 ` Но лучше этот код

