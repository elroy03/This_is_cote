from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def BFS(x: int, y: int, li: list, N: int, M: int):
    que = deque([y, x])
    while que:
        tmp = que.popleft()
        x = tmp[1]
        y = tmp[0]
        li[y][x] = 0
        for i in range(4):
            tx = x + dx[i]
            ty = y + dx[i]
            if tx < 0 or tx >= M or ty < 0 or ty >= N:
                continue
            if li[ty][tx] == 1:
                que.append([ty, tx])
                break


N, M = map(int, input().split())
li = list()
for n in range(N):
    li.append(list(map(int, input())))
cnt = 0
for n in range(N):
    for m in range(M):
        if li[n][m] == 1:
            BFS(n, m, li, N, M)
            cnt += 1
print(cnt)
