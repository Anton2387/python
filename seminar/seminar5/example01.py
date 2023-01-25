# расчитать нод(наибольший общий остаток от деления) двух чисел(быстрый и медленный способ)

def f(x, y):
    for i in range(x, 1, -1):
        if (x % i == 0) and (y % i == 0):
            return i

a = 25
b = 55

print(f(a,b))

# еще одно решение быстрый способ
a=20
b=58

if a < b :
    a, b = b, a

while b!=0:
    a, b = b, a % b

print(a)

a=20
b=75

# еще одно решение медленный способ

# a=20
# b=75

# while a != b:
#     if a > b:
#         a -= b
#     else:
#         b -= a

# print(a)