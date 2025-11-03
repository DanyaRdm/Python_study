5 != 4 # знак не равно, ТО есть тут TRUE = ВЕРНо знак не равно то есть 5 != 4 true

5 == 5 # знак равно, то есть тут TRUE = ВЕРНО это знак проверки, что действительно равно
# and - и то есть age < 15 and age> 10 Условия выполнится если оба параметра соблюдены
# or - или то есть age < 15 or age> 10 условие выполнится если один из параметров соблюдён
# not - не то есть not true = false not false = true
# примеры !=
print("введите возраст")
a = int(input())
if not a >= 18: # То есть если а не больше или равно 18, то вы ребенок
    print("children")
else:
    print("adult")

print("введите ваше имя")
name = input()
name_true = 'Даниил'
if name != name_true:
    print("Это не вы")
else:
    print("Доступ разрешён")
# .lower() преобразует все буквы в нижний регистр, то есть делает все буквы маленькими, маленькие останутся мал. большие станут мал. а цифры останутся цифрами
# пример с not == != и .lower() введем ПРивет будет привет
print("Введите логин")
login = input()
login_True = 'xaski'
print('Введите пароль цифрами')
password = int(input())
password_true = 12345678
if login.lower() == login_True and password == password_true:
    print('Доступ разрешён')
elif login.lower() != login_True and password == password_true:
    print("Введите правильный логин")
elif login.lower() == login_True and not password == password_true:
    print("Введите правильный пароль")
elif login.lower() != login_True and password != password_true:
    print("Доступ запрещён")
else:
    ("Доступ запрещён")