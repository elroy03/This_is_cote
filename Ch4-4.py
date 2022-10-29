M, N = map(int, input().split())
x, y, w = map(int, input().split())
li = [(0, 1), (1, 0), (0, -1), (-1, 0)]
tot = []
cnt = 1
for i in range(N):
    tot.append(list(map(int, input().split())))
tot[y][x] = 1

while True:
    tmp = 0
    for i in range(1, 5):
        d = li[w - i]
        if tot[y + d[1]][x + d[0]] == 0:
            x += d[0]
            y += d[1]
            tot[y][x] = 1
            w = 4 - i
            cnt += 1
            break
        if i == 4 and tot[y + d[1]][x + d[0]] == 1:
            tmp = 1
            break
    if tmp == 1:
        break
print(cnt)
