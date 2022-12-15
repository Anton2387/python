#value = None
#print(type(value))
a = 123
b = 1.23
print(a)
print(b)
value = 12334
#print(type(a))
#print(type(b))

s = 'hello world'
print(s) #вывод строки

print(a, '-',b, '-', s)
print('{1} - {2} - {0}'.format(a,b,s))
print(f'{a} - {b} - {s}')

f = True   # 
print(f)
k = False
print(k)

#задаем массив

list = ['1', '2', '3',] 
col = ['hello', 1,2,3.4, True]
print(list)
print(col)

# Ввод и вывод данных
# print, input

print('Введите а')
a = int (input())  # a = float (input()) вещественное значение
print('Введите b')
b = int (input())  # b = float (input()) вещественное значение
print(a, ' + ', b, ' = ', a+b)
print('{} {}'.format(a,b))
print(f'{a} {b}')

# Арифметические операции

a = 5
b = 6
c=a+b 
print(c)

# Логические операции

a = 3 > 1
print(a)

#Управляющие конструкции

a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b)