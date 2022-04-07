#003 - Longest Circular Road（★4）
#BFS ver.

#-----------------------------------
from collections import deque

#-----------------------------------
def bfs(x):
    deq = deque()
    deq.append(x)
    
    while len(deq) > 0:
        crr = deq.popleft()
        for nxt in E[crr]:
            if dist[nxt] != -1:
                continue
            dist[nxt] = dist[crr] + 1
            deq.append(nxt)

#-----------------------------------
N = int(input())

E = [[] for _ in range(N)]
for _ in range(N-1):
    A,B = map(int,input().split())
    E[A-1].append(B-1)
    E[B-1].append(A-1)

# STEP_01
dist = [-1]*N
dist[0] = 0
bfs(0)
s = dist.index(max(dist))

# STEP_02
dist = [-1]*N
dist[s] = 0
bfs(s)

ans = max(dist) + 1

print(ans)



