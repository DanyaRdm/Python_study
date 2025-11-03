python = 'python'
user = input("Введите слово")
if user.lower() == python:
    print("Верно")
elif user.lower() != python:
    print("Неверно")
else:
    print("Неверно")

print('Введите число')
x = int(input())
if x % 2 == 0:
    print('Четное число')
else:
    print("нечетное число")
# ТО есть тут показывается, что если пользователь введёт к примеру число 4 и его поделить на 2 то будет 2 то есть 0 четное
# А если ввести 5 то делить на 2 не получится, то есть 0 не будет, не четное число

print("Введите ваш возраст")
age = int(input())
print('введите страну проживания')
country = input()
country_true = 'россия'
if age >= 18 and country.lower() == country_true:
    print('Вы можете голосовать')
elif age >= 18 and country.lower() != country_true:
    print("Вы иногородний житель узнайте по поводу возможности голосовать В МФЦ")
elif age <= 17:
    print("Голосовать можно с 18 лет")
else:
    print("Проверьте правильность ввода данных")