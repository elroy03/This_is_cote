di = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'j': 8}
tmp = str(input())
x = int(di.get(tmp[0]))
y = int(tmp[1])
li = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
cnt = 0
for i in li:
    if ((0 < x + i[0]) and (x + i[0] < 8)) and ((0 < y + i[1]) and (y + i[1] < 8)):
        cnt += 1
print(cnt)
