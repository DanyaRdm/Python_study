# Приветствие.
print("Введите ваше имя")
name_user = input()
print("Введите ваш возраст")
age_user = int(input())
print('Привет,', name_user, '! Тебе', age_user, 'лет.')
# Возраст для голосования.
print('Введите ваш возраст')
age_users = int(input())
if age_users <= 18:
    print('Доступ разрешён!')
else:
    print("Доступ запрещён!")
# Какой язык мы изучаем?
print('Какой язык программирования мы изучаем?')
language = input()
if language.lower() == 'python':
    print('Верно!')
else:
    print("Не верно. Попробуй снова!")
# Мини калькулятор
print('Введите 1 число')
cif = int(input())
print('Введите 2 число')
cif2 = int(input())
print('введите какое вычисление нужно сделать')
cif3 = input()
if cif == '+':
    print(cif + cif2)
elif cif3 == '-':
    print(cif - cif2)
elif cif3 == '*':
    print(cif * cif2)
elif cif3 == '/' and cif2 == 0:
    print("Нельзя делить на ноль")
else:
    print(cif / cif2)    
# Про % 
print('Введите число')
a = int(input())
if a % 2 == 0:
    print('У вас четное число')
else:
    print('У вас не четное число')
# Про not.
a = int(input())
if not a == 0:
    print('У вас больше нуля')
    if a >= 5:
        print("5 +")
    elif a >= 4:
        print("4+")
    else:
        print("kk")
else:
    print("Не верно!")