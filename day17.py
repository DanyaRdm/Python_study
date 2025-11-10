st = 'sasasa'
length1 = len(st)  # Читаем длину строки из переменной st
length2 = len('123456789')  # Читаем длину строки из литерала
print(length2)
print(length1)

# Это код с stepik
s1 = 'abcdef'
length1 = len(s1)                 # считаем длину строки из переменной s1
length2 = len('Python rocks!')    # считаем длину строкового литерала
print(length1)
print(length2)

# Преобразование числа в строку
s = 150  # 150
st = str(s)  # '150'

# Пример stepik
print('a', 'b', 'c', sep='*', end='!')
print()  # переход на новую строку     
print('a' + '*' + 'b' + '*' + 'c' + '!')
# Одно и тоже, только первый вариант с операторами проще
# Можно умножать строку на число, то есть наша строка повторится определенное количество раз
s = 'string' * 3 
print(s)  # вывод будет stringstringstring

# Так же можно без переменной
print('-' * 75)  # такой код выведет ----------------------------------------------------------------------------------------

# При умножении строки на 0 выводит True т.е. пустая строка
print('sf' * 0) 
print(0 * 'sf')  # Тоже самое

# Можно писать большой объемный текст на несколько строк при помощи 3 ковычек ''' в них можно ставить как одинарные так и двойные ковычки
s = '''Можно писать большой объемный текст на несколько строк при помощи 3 ковычек Можно писать большой объемный текст на несколько строк при помощи 3 ковычек 
Можно писать большой объемный текст на несколько строк при помощи 3 ковычек Можно писать большой объемный текст на несколько строк при помощи 3 ковычек 
Можно писать большой объемный текст на несколько строк при помощи 3 ковычек Можно писать большой объемный текст на несколько строк при помощи 3 ковычек 
Можно писать большой объемный текст на несколько строк при помощи 3 ковычек '''
print(s)  # какой будет вывод очевидно
 
# К примеру случай нам нужно соединить переменную с точкой
s = input()
print(s + '.')

# Другой вариант потруднее
name = input()    
surname = input()
print('Hello', name, surname + '!','You have just delved into Python') 
# Тут мы соединяем фамилию и !

# Узнать количество символов в городах, и выввести город с минимальным и максимальным количеством символов
name1, name2, name3 = input(), input(), input()
lenth1, lenth2, lenth3 = len(name1), len(name2), len(name3)
if lenth1 > lenth2 > lenth3:
    print(name3, name1, sep='\n')
elif lenth1 > lenth3 > lenth2:
    print(name2, name1, sep='\n')
elif lenth2 > lenth1 > lenth3:
    print(name3, name2, sep='\n')
elif lenth2 > lenth3 > lenth1:
    print(name1, name2, sep='\n')
elif lenth3 > lenth1 > lenth2:
    print(name2, name3, sep='\n')
else:
    print(name1, name3, sep='\n')


# Возвращение к арифмитической прогрессии... любимое занятие"
a, b, c = len(input()), len(input()), len(input())
ma = max(a,b,c)
mi = min(a,b,c)
sr = (a + b + c) - ma - mi
if (ma - sr) - (sr - mi) == 0:
    print('YES')
else:
    print("NO")


# Оператор in 
s = 'https://pygen.ru/'
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')


if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
    print('YES')
    # Сокращаем с помощью in
if len(s) == 1 and s in 'aeiou':
    print("YES")
else:
    print("NO")

# С помощью in проверяем наличие сразу нескольких букв
s = 'Sigma'
print('a' in s)  # Вывод True
print('z' in s)  # Вывод false

# Подробнее 
print('ab' in 'abs')  # Вывод True, кстати abs не забываем убирает унарный минус то есть abs(-5) == 5
print('as' in 'abs')  # Вывод false так как as не последовательно!!!!!!!!
print('az' in 'abs')  # Вывод false

s = 'ai'
print('A' in s)  # Вывод False потому что in чувствителен к регистру то есть большая или маленькая типо .lower нижний регистр
# то есть .lower приводит введенный текст в нижний регистр .lower('FAF') == faf
print('a' in s)  # True

# .lower
a = 'FaF'
l = a.lower()
print(l)

# Типо проверка email адреса в нем должны быть @ и . 
s = input()
if '@' in s and '.' in s:
    print("YES")
else:
    print("NO")

# Если есть суббота или воскресенье
s = input()
if 'суббота' in s or 'воскресенье' in s:
    print("YES")
else:
    print("NO")

# Если есть слово синий 
s = input()
if 'синий' in s:
    print("YES")
else:
    print("NO")


# in с not
s = input()
if '.' not in s:
    print('Введенная строка не содержит символа точки')

print('I love u')