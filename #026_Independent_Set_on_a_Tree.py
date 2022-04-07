#026 - Independent Set on a Tree（★4）
# 二部グラフ

import sys
sys.setrecursionlimit(10**7)

#-----------------------------------
def rec(crr, pre, gr):
    if gr == 0:
        P[crr] = True
    else:
        Q[crr] = True
    
    for nxt in E[crr]:
        if nxt == pre:
            continue
        rec(nxt,crr,(gr+1)%2)

#-----------------------------------
N = int(input())

E = [[] for _ in range(N)]
for _ in range(N-1):
    A,B = map(int,input().split())
    E[A-1].append(B-1)
    E[B-1].append(A-1)

P = [False]*N #rem 0 #group-1
Q = [False]*N #rem 1 #group-2

rec(0,-1,0)
res = P if P.count(True) >= N//2 else Q # Trueが多い方のgroupから答えを出力

cnt = 0
for i,v in enumerate(res,1):
    if v:
        print(i)
        cnt += 1
    if cnt == N//2:
        break



