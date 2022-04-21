＃076 - Cake Cut（★3）
＃尺取り法ver.

from collections import deque

N = int(input())
A = list(map(int,input().split()))
W = sum(A)

A += A # ケーキ2個分
ans = "No"
deq = deque()
P = 0 #ケーキのサイズ
for l in range(2*N):
    # ケーキ追加
    deq.append(A[l])
    P += A[l]
    
    # ケーキ削除
    while len(deq) > 0 and  P > W/10:
        rem = deq.popleft()
        P -= rem
    
    if P == W/10:
        ans = "Yes"

print(ans)


