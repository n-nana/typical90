#012 - Red Painting（★4）
#2次元配列のunion-find（2次元データを1次元に変換する）

#---------------------------------------------------
class UnionFind:
    
    def __init__(self, n):
        self.par = [-1]*n
        self.rank = [0]*n
    
    #xのrootを取得
    def find(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    #xとyを併合
    def unite(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx,ry = ry,rx #rx: 親, ry: 子
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        
        return True
            
    #xとyが同一groupかどうか
    def check(self, x, y):
        return self.find(x) == self.find(y)

#---------------------------------------------------
H,W = map(int, input().split())
uf = UnionFind(H*W)

G = [[False]*W for _ in range(H)] # Red: True, White: False
dx = [-1,0,0,1]
dy = [0,-1,1,0]

Q = int(input())
for _ in range(Q):
    q,*A = map(int,input().split())
    
    # unite
    if q == 1:
        r,c = A[0]-1, A[1]-1
        G[r][c] = True
        u = r*W + c
        for i in range(4):
            R,C = r+dy[i], c+dx[i]
            if not (0 <= R < H and 0 <= C < W):
                continue
            v = R*W + C # 2次元データを1次元に変換
            if G[R][C]: # 隣接セルがTrue(Red)の場合、unite
                uf.unite(u,v)

    # find
    if q == 2:
        ra,ca,rb,cb = A[0]-1, A[1]-1, A[2]-1, A[3]-1
        U,V = ra*W + ca, rb*W + cb
        if G[ra][ca] and G[rb][cb] and uf.check(U,V):
            print("Yes")
        else:
            print("No")

