#Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

print('Введите цифру обозначающую день недели:')
a = input()

if a == '1':
    print('working day')
elif a == '2':
    print('working day')
elif a == '3':
    print('working day')
elif a == '4':
    print('working day')
elif a == '5':
    print('working day')
elif a == '6':
    print('day off')
elif a == '7':
    print('day off')
else:
    print('Такого дня недели не существует, попробуйте снова')