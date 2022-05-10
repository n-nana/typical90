#032 - AtCoder Ekiden（★3）
# 順列全探索ver.

import itertools

N = int(input())
G = []
for _ in range(N):
    A = list(map(int, input().split()))
    G.append(A)

M = int(input())
E = [[] for _ in range(N)]
for _ in range(M):
    x,y = map(int, input().split())
    E[x-1].append(y-1)
    E[y-1].append(x-1)
#-------------------------------------------
#ここまでは大体同じ

players = list(range(N))
INF = 10**5
ans = INF

for P in itertools.permutations(players,N):
    # 各順列で合計時間を計算
    res = G[P[0]][0]
    for i,v in enumerate(P):
        if i == 0:
            continue
        res += G[v][i]

    flag = False # flag = Falseの場合、特に問題なし
    for i in range(N-1):
        if P[i+1] in E[P[i]]:
            flag = True # NGの組み合わせがあればflag = Trueに
    res = INF if flag else res
    ans = min(res,ans)

print(-1 if ans == INF else ans)


