#079 - Two by Two（★3）

H,W = map(int, input().split())

A = []
for _ in range(H):
    a = list(map(int, input().split()))
    A.append(a)

B = []
for _ in range(H):
    b = list(map(int, input().split()))
    B.append(b)

dx = [0,1,1,0]
dy = [0,0,1,1]

ans = 0
for y in range(H-1):
    for x in range(W-1):
        diff = B[y][x] - A[y][x]
        ans += abs(diff)
        for i in range(4):
            Y = y + dy[i]
            X = x + dx[i]
            A[Y][X] += diff

flag = True
for y in range(H):
    if A[y][-1] != B[y][-1]:
        flag = False
for x in range(W):
    if A[-1][x] != B[-1][x]:
        flag = False

if flag:
    print("Yes")
    print(ans)
else:
    print("No")
