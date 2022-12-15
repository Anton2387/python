#Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения 
# not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) 
# для всех значений предикат.

print('Введите х:')
x = input()
print('Введите y:')
y = input()
print('Введите z:')
z = input()

left = not (x[0] or x[1] or x[2])
right = not x[0] and not x[1] and not x[2]
if left == right:
    print('Утверждение верно')
else:
    print('Утверждение ложно')