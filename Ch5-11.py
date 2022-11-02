from collections import deque

N, M = map(int, input().split())
gp = []
for n in range(N):
    gp.append(list(map(int, input())))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

que = deque()
que.append([0, 0])

while que:
    tmp = que.popleft()
    x = tmp[0]
    y = tmp[1]
    for i in range(4):
        tx = x + dx[i]
        ty = y + dy[i]

        if tx < 0 or tx >= N or ty < 0 or ty >= M:
            continue
        if gp[tx][ty] == 1:
            gp[tx][ty] = gp[x][y] + 1
            que.append((tx, ty))
print(gp[N - 1][M - 1])
