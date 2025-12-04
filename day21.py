# Счётчик чисел которые больше 10
counter = 0                                             # создаём переменную счётчика
for _ in range(10):
    num = int(input())
    if num > 10:                                        # при выполнении условия 
        counter = counter + 1                           # увеличиваем значение cчётчика

print('Было введено', counter, 'чисел, больших 10.')

# Помимо больше десяти добавим ещё 1 счетчик считающий кол во нулей
counter1 = 0
counter2 = 0
for _ in range(5):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1

print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )

# добавляем счётчик который посчитает сколько у нас чисел квадарат которых будет оканчиваться на 4
counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1

print(counter)

# Среднее значение из 10 чисел
total = 0
for _ in range(10):
    num = int(input())
    total = total + num

average = total / 10
print('Среднее значение равно', average)


# cмена значений
temp = x
x = 5
y = 3

# или
x, y = y, x

counter = counter + 1

counter = counter + num
counter / 10  # cp zn

num = int(input())
flag = True

for i in range(2, num):
    if num % i == 0:  #  если исходное число делится на какое-либо отличное от 1 и самого себя
        flag = False

if num == 1:
    print('Это единица, она не простая и не составная') 
elif flag == True:
    print('Число простое')
else:
    print('Число составное')

# Объясняю число простое если оно делится на 1 и на себя
# число составное если оно делится на себя, на 1 и на другое

a, b, c, d = 1, 2, 3, 4
a, b, c, d = b, c, d, a

print(a, b, c, d)  # вывод 2341

a, b = 3, 4
a, b = a + b, 2 * a

print(a, b)
# сначала выполнится а + b и 2 * a, а потом уже присовится ответ будет 7 6