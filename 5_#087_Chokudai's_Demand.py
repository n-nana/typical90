# 087 - Chokudai's Demand（★5）
# ワーシャルフロイド, 2分探索

INF = pow(10,12)

def Floyd_Warshall(x): #2分探索の境界がxのときの結果（条件を満たす組み合わせの数）を返す関数

    # 事前処理
    dist = [[INF]*N for _ in range(N)]
    for u in range(N):
        for v in range(N):
            if A[u][v] == -1:
                dist[u][v] = x
            else:
                dist[u][v] = A[u][v]

    # Main（ワーシャルフロイド）
    for k in range(N):
        for y in range(N):
            for x in range(N):
                dist[y][x] = min(dist[y][x], dist[y][k] + dist[k][x])

    # Main（count）
    cnt = 0
    for u in range(N-1):
        for v in range(u+1,N):
            if dist[u][v] <= P:
                cnt += 1
    return cnt

#----------------------------------------
N,P,K = map(int,input().split())

A = []
for _ in range(N):
    a = list(map(int,input().split()))
    A.append(a)

#----------------------------------------
# (1) c <= Kとなる最小のxをLとする
mx = INF
mn = 0
for i in range(60):
    mid = (mx+mn)//2
    c = Floyd_Warshall(mid)
    if c > K:
        mn = mid
    else:
        mx = mid
L = mn

#----------------------------------------
# (2) c < Kとなる最小のxをRとする
mx = INF
mn = 0
for i in range(60):
    mid = (mx+mn)//2
    c = Floyd_Warshall(mid)
    if c >= K:
        mn = mid
    else:
        mx = mid
R = mn

#----------------------------------------
if R == INF-1: # INF-1で判定
    if L == INF-1: # INF-1で判定
        ans = 0
    else:
        ans = "Infinity"
else:
    ans = R - L
    
print(ans)
