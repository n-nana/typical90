#011 - Gravy Jobs（★6）
#処理する順番を工夫したDP

N = int(input())

A = []
for _ in range(N):
    d,c,s = map(int,input().split())
    A.append([d,c,s])
A.sort(key = lambda x: x[0])
    
dp = [[0]*5001 for _ in range(N+1)]
for i in range(N):
    d,c,s = A[i]
    for l in range(1,5001):
        dp[i+1][l] = max(dp[i+1][l], dp[i][l])
        r = l + c - 1
        if r <= d:
            dp[i+1][r] = max(dp[i+1][r], dp[i][l-1] + s)
        
ans = max(dp[-1])
print(ans)

