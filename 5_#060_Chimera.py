#060 - Chimera（★5）
#LIS（最長増加部分列）

import bisect

N = int(input())
A = list(map(int,input().split()))

# 左からLIS
L = [A[0]]
P = [1] # i番目を選ぶ場合のLIS
for i in range(1,N):
    idx = bisect.bisect_left(L, A[i])
    if idx == len(L):
        L.append(A[i])
    else:
        L[idx] = A[i]
    P.append(idx+1) 

# 右からLIS
A.reverse()
R = [A[0]]
Q = [1] # i番目を選ぶ場合のLIS
for i in range(1,N):
    idx = bisect.bisect_left(R, A[i])
    if idx == len(R):
        R.append(A[i])
    else:
        R[idx] = A[i]
    Q.append(idx+1) 
Q.reverse()
    
ans = 0
for i in range(N):
    ans = max(ans, P[i]+Q[i]-1)

print(ans)
