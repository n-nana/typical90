# 043 - Maze Challenge with Lack of Sleep（★4）
# 枝刈BFS ver.(350msecくらいまでおとせた)

from collections import deque

INF = float("inf")

H,W = map(int,input().split())
sy,sx = map(lambda x: int(x) - 1, input().split())
gy,gx = map(lambda x: int(x) - 1, input().split())
S = [input() for _ in range(H)]

dx = (-1,0,0,1)
dy = (0,-1,1,0)

# 枝刈ver.では結果を4方向で管理しなくてok
res = [[INF]*W for y in range(H)]

deq = deque()
for i in range(4):
    res[sy][sx] = -1
    deq.append((sx,sy))

while len(deq) > 0:
    x,y = deq.popleft()
    cnt = res[y][x]
    
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        
        # ここから枝刈りBFS（いける（while True）ならどんどん進む, 01-BFSのappendleftみたいなかんじ）
        while True:
            if not (0 <= X < W and 0 <= Y < H):
                break
            if S[Y][X] == "#":
                break
            if res[Y][X] < cnt + 1:
                break
                
            if res[Y][X] > cnt + 1:
                res[Y][X] = cnt + 1
                deq.append((X,Y))
            X += dx[i]
            Y += dy[i]

print(res[gy][gx])

#for i in range(H):
#    print(res[i])
