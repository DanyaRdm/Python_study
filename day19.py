for i in range(10):
    print('Привет')  #  10 раз в ряд напишет Слово Привет, то есть range это диапозон сколько раз
# for название_переменной_цикла in range(количество_повторений): блок кода
for i in range(5):
    num = int(input())
    print('Квадрат вашего числа равен:', num * num)

print('Цикл завершен')
# То есть в этой программе мы установили кол-во раз сколько повторится цикл,
# и 5 раз вводим число которое возводится в квадрат
print("A")
print("B")

for i in range(5):
    print("C")
    print("D")

print("E")
# В этой программе ответ будет АBCDCDCDCDCDE, так как мы не обращаемся к переменной

for i in range(2):
    print('we will')

print('rock you') 
# we will we will rock you

for i in range(10):
    print('Python is awesome!')
# 10 раз выведет текст с новой строки

for i in range(10):
    print(i, '-- Привет')

for i in range(10):
    print(i)
for number in range(10):
    print(number)
# оба этих цикла покажут 0 1 2 3 4 5 6 7 8 9
# То есть цикл fоr а i это просто название переменной которая изначально несет в себе 0 
# в цикле for можно поставить переменную _ вместо i, и это не будет синтаксической ошибкой
for _ in range(5):
    print('Python - awesome!')

# Если нужно написать цифры от 1 до 100 в ряд можно использовать этот код
for i in range(100):
    print(i + 1)