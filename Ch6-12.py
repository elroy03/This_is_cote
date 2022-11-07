N, K = map(int, input().split())

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1 = sorted(arr1)
arr2 = sorted(arr2, reverse=True)

for i in range(K):
    if arr1[i] >= arr2[i]:
        break
    tmp = arr1[i]
    arr1[i] = arr2[i]
    arr2[i] = tmp
print(sum(arr1))
