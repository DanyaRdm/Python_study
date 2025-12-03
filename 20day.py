for i in range(4, 5):  # range с 2 параметрами
    print('hi')
for i in range(25, 99, 3):  # range с 3 параметрами
    if i % 10 == 7:
        print(i)

for i in range(30, 25, -1):  # range с 3 параметрами, но в обратной последовательности
    print(i)

for i in range(5, 0, -1):
    print(i, end=' ')
print('Взлетаем!!!')

# напомню
a = '''множественное написание
на несколько 
строк 3 ковычками'''

# если вводят 2 целых числа, и нужно чтобы выдало от 1 введенного до 2 введенного включительно
# можно делать так
a = int(input())
b = int(input())
for i in range(a, b + 1):
    print(i)

a = int(input())
b = int(input())
if a > b:
    for i in range(a, b+1):
        print(i)
elif b > a:
    for i in range(a, b -1 , -1):
        print(i)
else:
    print(a)

# даны 2 числа нужно вывести только нечетные включая 1 число
a = int(input())
b = int(input())  
for i in range(a - 1 + a % 2, b - 1, - 2):
    print(i)
# надо ещё подумать над этим примером



m = int(input())
n = int(input())
if m == n:
    print(m)
else:
    for num in range(m, n + 1):
        if num % 17 == 0 or num % 10 == 9 or (num % 3 == 0 and num % 5 == 0):
            print(num)
# этот пример тоже обдумать ещё раз



a = int(input())
for i in range(1, 11):
    print(a, 'x', i, '=', a * i)

# таблица умножения на введенное число





