#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input('n = '))
list = [1]
for i in range(n-1):
    list.append(list[i] * ((1+1/n)**n))
print(list)

sum1=0
for i in list:
    sum1 += i
print('Сумма последовательности (1+1/n)**n =', sum1)