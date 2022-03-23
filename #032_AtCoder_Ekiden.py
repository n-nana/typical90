#032 - AtCoder Ekiden（★3）
#722ms@Pypy3, TLE@Python3

import sys
sys.setrecursionlimit(10**7)

#--------------------------------------
def dfs(k,cnt,res):
    global ans
    
    done[k] = True
    
    if cnt == N-1:
        ans = min(res,ans)
        #print(res)
        return
    
    for nxt in range(N):
        if done[nxt]:
            continue
        if nxt in E[k]: # NGの順列の場合は何もしない
            continue
        dfs(nxt,cnt+1,res+G[nxt][cnt+1])
        done[nxt] = False # 再帰から戻ったときはstatusをFalseに戻す
    
#--------------------------------------
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

INF = 10**5
ans = INF

for i in range(N):
    done = [False]*N
    dfs(i,0,G[i][0])
    
print(-1 if ans == INF else ans)



