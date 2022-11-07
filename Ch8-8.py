N, M = map(int, input().split())
li = []
for n in range(N):
    li.append(int(input()))
dp = [10001] * (M + 1)
dp[0] = 0

for i in range(N):
    for j in range(li[i], M + 1):
        if dp[j - li[i]] != 10001:
            dp[j] = min(dp[j], dp[j - li[i]] + 1)

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
