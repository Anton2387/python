#Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('N = '))
list = [1]
count=2
for i in range(n-1):
    list.append(list[i] * count)
    count+=1
print(list)
