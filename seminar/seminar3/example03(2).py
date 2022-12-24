anton = "anton"

n = 7
list = ['222anton456', 'a1n1t1o1n1', '0000a0000n00t00000o000000n', 'gylfole', 'richard', 'anto0n', 'anton']
find = []

for i in range(n):
    count = 0
    for j in range(len(list[i])):
        if anton[count] == list[i][j]:
            count += 1
        if count == 5:
            find.append(i+1)
            break

print(find)