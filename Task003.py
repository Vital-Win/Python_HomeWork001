# 3. Напишите программу, которая принимает на вход 
# координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0, 
# и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

# Пример:
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3

x = int(input('Введите число X ≠ 0: '))
y = int(input('Введите число Y ≠ 0: '))

if x == 0 and y == 0:
    print('Не выполнено условие: X ≠ 0 и Y ≠ 0')
elif x == 0:
    print('Не выполнено условие: X ≠ 0')
elif y == 0:
    print('Не выполнено условие: Y ≠ 0')
elif x > 0 and y > 0:
    print('Точка находится в 1-ой четверти')
elif x < 0 and y > 0:
    print('Точка находится во 2-ой четверти')
elif x < 0 and y < 0:
    print('Точка находится во 3-й четверти')
elif x > 0 and y < 0:
    print('Точка находится во 4-ой четверти')      