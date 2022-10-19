N, M = map(int, input().split())

maxa = 0

for i in range(N):
    li = list(map(int, input().split()))
    tmp = min(li)
    if tmp > maxa:
        maxa = tmp

print(maxa)
