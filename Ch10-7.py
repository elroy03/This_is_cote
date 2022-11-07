def Parent_F(parent: list, a: int):
    if parent[a] != a:
        parent[a] = Parent_F(parent, parent[a])
    return parent[a]


def Union_P(parent: list, a: int, b: int) -> None:
    a: int = Parent_F(parent, a)
    b: int = Parent_F(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N, M = map(int, input().split())
parent = [0] * (N + 1)
for i in range(N + 1):
    parent[i] = i

for _ in range(M):
    q, a, b = map(int, input().split())
    if q == 0:
        Union_P(parent, a, b)
    elif q == 1:
        if Parent_F(parent, a) == Parent_F(parent, b):
            print("YES")
        else:
            print("NO")
