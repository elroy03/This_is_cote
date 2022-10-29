N = int(input())
A = list(map(str, input().split()))
x, y = 1, 1
for i in A:
    if i == 'L':
        if x == 1:
            continue
        else:
            x -= 1
    elif i == 'R':
        if x + 1 > N:
            continue
        else:
            x += 1
    elif i == 'U':
        if y == 1:
            continue
        else:
            y -= 1
    elif i == 'D':
        if y + 1 > N:
            continue
        else:
            y += 1
print(y, x)
