a = int(input())  # 1
b = int(input())  # 2
c = (a + b) ** 2
n = a ** 2 + b ** 2
print("Квадрат суммы", a, "и", b, 'равен', c)
print("Сумма квадратов", a, "и", b, 'равна', n)

# На входе данные 5 должно выдать 5 + 55 + 555 
a = int(input())  # 1
b = str(a) + str(a)
c = str(a) + str(a) + str(a)
n = int(b) + int(c) + int(a)
print(n)


a = int(input())  # 1423
b = a // 1000  # 1
c = (a // 100) % 10  # 4 
n = (a % 100) // 10  # 2
m = a % 10  # 3
if b + m == c - n:
    print("ДА")
else:
    print('НЕТ')

# Функции min и max:
a = int(input())  # 1
b = int(input())  # 2
c = int(input())  # 3
n = int(input())  # 4
print(min(a,b,c,n))  # 1
print(max(a,b,c,n))  # 4

# Слон ходит только по вертикали или горизонтали
x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())

if (x1 - y1 == x2 - y2) or (x1 + y1 == x2 + y2):
    print('YES')
else:
    print('NO')