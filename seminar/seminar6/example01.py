#1.Вводится список целых чисел в одну строчку через пробел.
#  Необходимо оставить в нем только двузначные числа. 
# Реализовать программу с использованием функции filter.
#  Результат отобразить на экране в виде последовательности 
# оставшихся чисел в одну строчку через пробел.

# пример - 8 11 0 -23 140 1 => 11 -23

# numbers = list(map(int, input().split()))
# # result = [i for i in numbers if 10 <= abs(i) <= 99]
# result2 = list(filter(lambda i: 10 <= abs(i) < 100, numbers))
# # print(result)
# print(result2)


print(*filter(lambda x: len(str(abs(int(x)))) == 2, input().split()))