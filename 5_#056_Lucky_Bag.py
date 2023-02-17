# 056 - Lucky Bag（★5）

N,S = map(int,input().split())

dp = [[0]*(S+3) for _ in range(N+3)]
dp[0][0] = 1 # 0: False, 1: Trueとした

P = []
for i in range(N):
    A,B = map(int,input().split())
    P.append([A,B])
    for j in range(S):
        if dp[i][j] == 0: continue
        if j+A <= S: dp[i+1][j+A] = 1
        if j+B <= S: dp[i+1][j+B] = 1

# 復元
if dp[N][S] == 1:
    res = []
    nxt = S
    for i in range(N-1,-1,-1):
        A,B = P[i]
        for j in range(S):
            if dp[i][j] == 0: continue
            if j+A == nxt:
                nxt = j
                res.append("A")
                break
            elif j+B == nxt:
                nxt = j
                res.append("B")
                break
    res.reverse()
    print("".join(res))
else: print("Impossible")
    
