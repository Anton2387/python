# Напишите программу, которая найдёт 
# произведение пар чисел списка. 
# Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers = [2, 3, 4, 5, 6]

l = len(numbers)//2 + 1
if len(numbers) % 2 != 0:
    len(numbers)//2
    new_lst = [numbers[i]*numbers[len(numbers)-i-1] for i in range(l)]
    print(new_lst)


