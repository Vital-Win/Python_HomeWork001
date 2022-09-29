# 4.Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

quarter_number = int(input('Введите номер четверти: '))

if quarter_number == 1:
    print(f'Диапазон возможных координат точек в {quarter_number}-й четверти: X > 0 и Y > 0')
elif quarter_number == 2:
    print(f'Диапазон возможных координат точек в {quarter_number}-й четверти: X < 0 и Y > 0')
elif quarter_number == 3:
    print(f'Диапазон возможных координат точек в {quarter_number}-й четверти: X < 0 и Y < 0')
elif quarter_number == 4:
    print(f'Диапазон возможных координат точек в {quarter_number}-й четверти: X > 0 и Y < 0')
else:
    print('Введенная четверть не существует')