#Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка.
#Пример:
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

print('Введите любую координату х:')
x = int (input())
print('Введите любую координату y:')
y = int (input())

if x > 0 and y > 0:
    print('Первая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
elif x < 0 and y < 0:
    print('Третья четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
else:
    print('Вводить ноль нельзя!')