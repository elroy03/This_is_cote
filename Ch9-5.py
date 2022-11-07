import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
N, M, C_start = map(int, input().split())

distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]

for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(C_start)

cnt = -1
maxd = 0
for i in distance:
    if i != INF:
        cnt += 1
        maxd = max(maxd, i)
print(cnt, maxd)
