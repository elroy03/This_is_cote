N = int(input())
dic = []
for i in range(N):
    tmp = str(input())
    tmp2 = int(input())
    dic.append([tmp, tmp2])

arr = sorted(dic, key=lambda x: dic[1])

for i in range(N):
    print(arr[i][0], end=' ')
