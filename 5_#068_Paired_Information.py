# 068 - Paired Information（★5）
# クエリ先読み
# parityで答えを分類
# Union-Find
# segment-tree解法（https://atcoder.jp/contests/typical90/editorial/3221）# 確認前

class UnionFind:
    
    def __init__(self, n):
        self.par = [-1]*n # 要素の根（親）
        self.rank = [0]*n # 要素が属している木の高さ
        self.siz = [1]*n # 要素が属している木の大きさ（要素数）

    # xのroot(Find)
    def root(self, x):
        if self.par[x] == -1:
            return x
        else:
            self.par[x] = self.root(self.par[x])
            return self.par[x]
    
    # xとyをmerge(Union)
    def merge(self, x, y):
        rx,ry = self.root(x), self.root(y)
        if rx == ry: return False
        if self.rank[rx] < self.rank[ry]:
            rx,ry = ry,rx # rx: 親, ry: 子
        self.par[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1        
        self.siz[rx] += self.siz[ry]
        return True
            
    # xとyが同一のgroupかどうか
    def issame(self, x, y):
        return self.root(x) == self.root(y)
    
    # xが含まれる木のサイズ
    def size(self, x):
        return self.siz[self.root(x)]

#---------------------------------------------------
N = int(input())
uf = UnionFind(N)

# A[i]とA[i+1]の差
diff = [0]*(N-1)

res = []
Q = int(input())
for _ in range(Q):
    T,X,Y,V = map(int,input().split())
    X -= 1
    Y -= 1
    if T == 0: # merge query
        uf.merge(X,Y)
        diff[X] = V
    elif T == 1: # answer query
        if uf.issame(X,Y):
            res.append([X,Y,V])
        else:
            res.append(False) # この時点でansが不明

A = [0] # A[0] == 0とした場合のA[i]の値, parityが同じなら値の変化方向が同じ
for i in range(N-1):
    A.append(diff[i] - A[-1])
#print(A)
    
for r in res:
    if r == False:
        print("Ambiguous")
    else:
        x,y,vx = r # idx-x, idx-y, val-x
        d = vx - A[x] # 基準値:A[x]と変化後の値:vx の差
        if x%2 == y%2: # parityが同じ場合
            vy = A[y] + d
        else: # parityが異なる場合
            vy = A[y] - d
        print(vy)
        
        
