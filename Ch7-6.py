import sys


def BS(x: int, li: list):
    start = 0
    end = len(li) - 1
    while start <= end:
        mid = (start + end) // 2
        if li[mid] == x:
            return True
        if x > li[mid]:
            start = mid + 1
        elif x < li[mid]:
            end = mid - 1
    return False


N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
arr1 = sorted(arr1)

for i in arr2:
    if BS(i, arr1):
        print("yes", end=' ')
    else:
        print("no", end=' ')
