#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#Пример:
#- 6782 -> 23
#- 0,56 -> 11

number = int(input('Введите вещественное число = '))
count = len(str(number))
sum1=0
while count > 0:
    i = number%10
    sum1 += i
    number //= 10
    count -= 1
else:
    print(sum1)
