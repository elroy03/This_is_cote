N, M = map(int, input().split())
li = list(map(int, input().split()))

start = 0
end = max(li)
mins = 0
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for x in li:
        if x > mid:
            tmp += (x - mid)
    if tmp < M:
        end = mid - 1
    else:
        mins = mid
        start = mid + 1
print(mins)
