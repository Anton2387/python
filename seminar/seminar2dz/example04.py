#Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в отдельном списке
# (пример n=4, lst1=[4,-2,1,3] - список на основе n, 
# а позиции элементов lst2=[3,1].

from random import randint
N = int(input('N = '))
list = []
for i in range(N+1):
    list.append(randint(-N, N))
print(list)

x = int(input('Введите номер позиции от 0 до N: '))
y = int(input('Введите номер второй от 0 до N: '))

result2 = list[x] * list[y]
print('Произведение элементов =', result2)