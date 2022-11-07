N = int(input())
li = []
for i in range(N):
    li.append(int(input()))

arr = sorted(li, reverse=True)

for i in arr:
    print(i, end=' ')
