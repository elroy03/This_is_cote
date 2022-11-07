def Parent(parent, a):
    if parent[a] != a:
        parent[a] = Parent(parent, parent[a])
    return parent[a]


def Union(parent, a, b):
    a = Parent(parent, a)
    b = Parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
edges = []
parent = [i for i in range(N + 1)]
result = 0
maxc = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

for i in edges:
    if Parent(parent, i[1]) != Parent(parent, i[2]):
        Union(parent, i[1], i[2])
        result += i[0]
        maxc = max(maxc, i[0])

print(result - maxc)
