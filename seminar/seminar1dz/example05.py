#Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

print('Введите первую координату первой точки:')
x1 = int (input())
print('Введите вторую координату первой точки:')
y1 = int (input())
print('Введите первую координату второй точки:')
x2 = int (input())
print('Введите вторую координату второй точки:')
y2 = int (input())

from math import sqrt
result = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(result)

result2 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(result2)