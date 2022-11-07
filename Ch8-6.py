N = int(input())
li = list(map(int, input().split()))
dp = [0] * 100

dp[0] = li[0]
dp[1] = max(dp[0], li[1])

for i in range(2, N):
    dp[i] = max(dp[i - 1], dp[i - 2] + li[i])

print(dp[N - 1])
