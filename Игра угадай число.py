a = 21
b = int(input("Угадайте число"))
if b > a:
    print("Неверно")
elif b < a:
    print("Неверно")
else:
    print("Верно!!!")

temperature = float(input("Введите температуру"))
if temperature >= 30:
    print("На улице очень жарко")
elif temperature >= 20:
    print("На улице тепло")
elif temperature >= 10:
    print("На улице прохладно")
elif temperature >= 0:
    print("На улице холодно")
elif temperature >= -10:
    print("На улице заморозки")
elif temperature >= - 20:
    print("На улице мороз")
else:
    print("Одевайтесь как можно теплее")