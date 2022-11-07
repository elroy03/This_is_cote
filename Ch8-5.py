x = int(input())

dp = [0] * (x + 1)

for X in range(2, x + 1):
    dp[X] = dp[X - 1] + 1
    if X % 5 == 0:
        dp[X] = min(dp[X], dp[X // 5] + 1)
    if X % 3 == 0:
        dp[X] = min(dp[X], dp[X // 3] + 1)
    if X % 2 == 0:
        dp[X] = min(dp[X], dp[X // 2] + 1)

print(dp[x])
