# 062 - Paint All（★6）
# 逆から貪欲, queue
# ABC329E - Stamp / https://atcoder.jp/contests/abc329/tasks/abc329_e

from collections import deque

N = int(input())

E = [set() for _ in range(N)]
for i in range(N):
    a,b = map(int,input().split())
    E[a-1].add(i)
    E[b-1].add(i)
    
done = [False]*N
ans = []
deq = deque()
for i in range(N):
    if i in E[i]:
        done[i] = True
        ans.append(i+1)
        deq.append(i)

while deq:
    crr = deq.popleft()
    for nxt in E[crr]:
        if done[nxt]:
            continue
        done[nxt] = True
        ans.append(nxt+1)
        deq.append(nxt)

if len(ans) == N:
    for i in range(N):
        print(ans[~i])
else:
    print(-1)
    
