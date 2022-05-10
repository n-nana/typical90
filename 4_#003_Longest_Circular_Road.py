#003 - Longest Circular Road（★4）

import sys
sys.setrecursionlimit(10**7)

#-----------------------------------
def rec(crr, pre, cnt):
    dist[crr] = cnt
    
    for nxt in E[crr]:
        if nxt == pre:
            continue
        rec(nxt, crr, cnt+1)
    
#-----------------------------------
N = int(input())

E = [[] for _ in range(N)]
for _ in range(N-1):
    A,B = map(int,input().split())
    E[A-1].append(B-1)
    E[B-1].append(A-1)

# STEP_01（端点（いずれか一つでok）の探索）
dist = [-1]*N
rec(0,-1,0) # 今いるところ, 前にいたところ, 通った辺の数
s = dist.index(max(dist)) # 辺の数が最大だったノードを次の始点にする

# STEP_02（sからの辺の数を計測）
dist = [-1]*N
rec(s,-1,0)
ans = max(dist) + 1

print(ans)

