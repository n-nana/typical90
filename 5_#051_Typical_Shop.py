#051 - Typical Shop（★5）
#半分全列挙
#二分探索
#（参考）https://algo-logic.info/split-and-list/

import bisect

N,K,P = map(int,input().split())
A = list(map(int,input().split()))

A1 = A[:N//2] #グループ01
N1 = len(A1)
A2 = A[N//2:] #グループ02
N2 = len(A2)

#bit全探索(Gr.01)
B1 = []
for i in range(1<<N1):
    tmp = 0
    c1 = 0
    for j in range(N1):
        if (i>>j)&1 == 1:
            tmp += A1[j]
            c1 += 1
    B1.append([tmp,c1])
    
mx = 2*(10**6)
#bit全探索(Gr.02, 要素数でSub-Gr.に分類)
B2 = [[] for _ in range(mx)]
for i in range(1<<N2):
    tmp = 0
    c2 = 0
    for j in range(N2):
        if (i>>j)&1 == 1:
            tmp += A2[j]
            c2 += 1
    B2[c2].append(tmp) #c2: Sub-Gr.

for i in range(mx): #昇順sort（2分探索用）
    B2[i].sort()

res = 0
for i in range(1<<N1):
    b1 = B1[i][0]
    n1 = B1[i][1] #Gr.01の要素数
    n2 = K - n1 #Gr.02の要素数
    cnt = bisect.bisect_right(B2[n2], P-b1) # P以下の要素をcount
    res += cnt

print(res)    
