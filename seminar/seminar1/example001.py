# 1. Напишите программу, 
# которая принимает на вход два числа 
# и проверяет, является ли одно число 
# квадратом другого.
#*Примеры:* 
#- 5, 25 -> да
#- 4, 16 -> да
##- 25, 5 -> да
#- 8,9 -> нет

print('Введите а')
a = int (input())  # a = float (input()) 
print('Введите b')
b = int (input())  # b = float (input())
c = a*a
if c == b:
    print('yes')
else:
    print('no')