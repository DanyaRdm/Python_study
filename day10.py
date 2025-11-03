# Нужно сделать код который определяет одинаковы ли все 3 числа или нет
num = int(input())  # Введем условно 934
d3 = num % 10  # 4
d2 = num % 100 // 10  # 3
d1 = num // 100  # 9
if d3 != d2 and d3 != d1 and d2 != d1:
    print('Цифры различны')
else:
    print('Цифры не различны')

a = int(input())
if a <= -3 or a >= 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

# Решения со степика индивидумов
n = int(input())
print('Принадлежит' if -30 < n <= -2 or 7 < n <= 25 else 'Не принадлежит')

print('Принадлежит' if int(input()) in (list(range(-29, -1)) + list(range(8, 26))) else 'Не принадлежит')
# Что такое range и list я ещё не изучал, но мой код на 5 строк, а этот на 1((

# Задача число красивое Yes если оно четырехзначное и делится на 7 или на 17
a = int(input())
if 1000 <= a < 1000 and (a // 7 == 0 or a // 17 == 0):
    print("YES")
else:
    print("NO")

# У нас есть данные, ладья ходит только по вертикали или по горизонтали от 1 до 8
# То есть она ходи по горизонтали значит вертикаль остается в той же клетке
# А если ходит по вертикали значит горизонталь в той же клетке
numstolb_1 = int(input())
numstroka_1 = int(input())
numstolb_2 = int(input())
numstroka_2 = int(input())
if (numstolb_1 == numstolb_2 and numstroka_1 != numstroka_2) or (numstroka_1 == numstroka_2 and numstolb_1 != numstolb_2):
    print("YES")
else:
    print("NO")