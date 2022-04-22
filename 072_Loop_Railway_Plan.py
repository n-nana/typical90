#072 - Loop Railway Plan（★4）

import sys
sys.setrecursionlimit(10**7)

def rec(y,x,c):

    if y == sy and x == sx and visited[y][x]:
        ans[0] = max(c, ans[0])
        return
    
    for i in range(4):
        Y,X = y+dy[i], x+dx[i]
        if not (0 <= Y < H and 0 <= X < W):
            continue
        if G[Y][X] == "#":
            continue
        if visited[Y][X]:
            continue
        visited[Y][X] = True
        rec(Y,X,c+1)
        visited[Y][X] = False # わすれがちな処理、、

#------------------------------------
H,W = map(int,input().split())
G = []
for _ in range(H):
    g = input()
    G.append(g)

dx = [-1,0,0,1]
dy = [0,-1,1,0]

res = -1
for i in range(H):
    for j in range(W):
        ans = [-1] # リストにしている
        visited = [[False]*W for _ in range(H)]
        sy,sx = i,j
        rec(i,j,0)
        res = max(ans[0], res)

print(res if res > 2 else -1)




