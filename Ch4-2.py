N = int(input())
cnt1 = 1575
cnt2 = 3600

if N < 3:
    print(cnt1 * (N + 1))
elif N < 12:
    print(cnt1 * N + cnt2)
elif N < 22:
    print(cnt1 * (N - 1) + cnt2 * 2)
else:
    print(cnt1 * (N - 2) + cnt2 * 3)

# 반복문으로 푼 경우.
# cnt = 0
# for i in range(N + 1):
#     for j in range(60):
#         for k in range(60):
#             if '3' in str(i) + str(j) + str(k):
#                 cnt += 1
# print(cnt)
