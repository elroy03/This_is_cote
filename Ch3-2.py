N, M, K = map(int, input().split())
li = list(map(int, input().split()))
li.sort(reverse=True)
cnt = 0
a = 0
for i in range(M):
    if a == K:
        cnt += li[1]
        a = 0
    else:
        cnt += li[0]
        a += 1
print(cnt)

# 수열을 파악하여 해결
# N, M, K = map(int, input().split())
# li = list(map(int, input().split()))
# li.sort(reverse=True)
#
# cnt = int(M/(K+1)) * K
# cnt += M % (K+1)
#
# result = 0
# result += (cnt * li[0])
# result += (M-cnt) * li[1]
#
# print(result)
