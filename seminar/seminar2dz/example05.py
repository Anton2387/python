#Реализуйте алгоритм перемешивания списка. 
#(рандомно поменять местами элементы списка между собой)

from random import randint
N = int(input('N = '))
list = []
for i in range(N):
    list.append(randint(0, N))
print(list)

import random
random.shuffle(list)
print(list)