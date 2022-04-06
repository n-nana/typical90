#003 - Longest Circular Road（★4）

# 以下、ためしたいことなどメモ
# （最長距離をBFSで算出）
# DFSでvisited管理ではなくpre-visitedを使う
# 始点からの距離情報をリストでもつ（他の問題とかで応用がききそう

import sys
sys.setrecursionlimit(10**7)

#-----------------------------------
def rec(n,d): # 現在のnode, 始点からの距離
    global edge # 最長距離のnode番号と距離を管理（変数名が微妙、、
    
    visited[n] = True
    if d > edge[1]: # 更新できるなら更新
        edge = [n,d]
#    print(edge)
    for nxt in E[n]:
        if visited[nxt]:
            continue
        rec(nxt,d+1)
    
#-----------------------------------
N = int(input())

E = [[] for _ in range(N)]
for _ in range(N-1):
    A,B = map(int,input().split())
    E[A-1].append(B-1)
    E[B-1].append(A-1)

# フェーズ01（端点（いずれか一つでok）の探索）
visited = [False]*N
edge = [0,0] #node_0から最も遠いnode（いずれか一点）, node_0からの距離
rec(0,0) #始点,距離
#print(edge)
s = edge[0] # ←端点はこれ
#print()

# フェーズ02（フェーズ01で求めた端点からの最長距離を計測）
# やることはフェーズ01と同じ（始点が端点にかわるだけ
visited = [False]*N
edge = [0,0] #node_0から最も遠いnode（いずれか一点）, node_0からの距離
rec(s,0)
#print(edge)
ans = edge[1] + 1 # 追加する辺の分で+1

print(ans)


