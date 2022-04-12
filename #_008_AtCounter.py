# 008 - AtCounter（★4）

MOD = 10**9 + 7

N = int(input())
S = input()

A = "atcoder"
M = len(A)

dp = [[0]*(M+5) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(M+1):
        if j < M and S[i] == A[j]:
            dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
        dp[i+1][j] = max(dp[i][j], dp[i+1][j])
        dp[i+1][j] %= MOD

print(dp[-1][M]%MOD)

#print()
#for i in range(N+1):
#    print(dp[i])

