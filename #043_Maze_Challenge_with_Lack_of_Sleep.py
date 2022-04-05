# 043 - Maze Challenge with Lack of Sleep（★4）
# 01-BFSの問題（類題ABC246E - Bishop 2とか）
# TLEがとれなかったが、3次元リストを1次元に落とすことで通せた、、
#（コメントアウトで残しているコードは3次元のときのもの）

from collections import deque

#INF = float("inf")
INF = 10**7

H,W = map(int,input().split())
sy,sx = map(lambda x: int(x) - 1, input().split())
gy,gx = map(lambda x: int(x) - 1, input().split())
S = [input() for _ in range(H)]

dx = (-1,0,0,1)
dy = (0,-1,1,0)

# 4方向分のres
#res = [[[INF]*W for y in range(H)] for i in range(4)]
res = [INF]*W*H*4

deq = deque()
# 初期値
for i in range(4):
#    res[i][sy][sx] = 0
    res[W*H*i + W*sy + sx] = 0
    deq.append((sx,sy,i))

while len(deq) > 0:
    x,y,r = deq.popleft()
#    cnt = res[r][y][x]
    cnt = res[W*H*r + W*y + x]
    
    if x == gx and y == gy:
#        print(res[r][y][x])
        print(res[W*H*r + W*y + x])
        break
    
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        if not (0 <= X < W and 0 <= Y < H):
            continue
        if S[Y][X] == "#":
            continue
        c = cnt
        if i != r: # 方向が異なる場合はcost +1
            c += 1
#        if res[i][Y][X] > c:
#            res[i][Y][X] = c
        if res[W*H*i + W*Y + X] > c:
            res[W*H*i + W*Y + X] = c
            if i == r: # 方向が同じ場合はappendleftで優先的に取り出す
                deq.appendleft((X,Y,i))
            else: # 方向が異なる場合は後ろに追加（一般的なBFSとおなじ
                deq.append((X,Y,i))

