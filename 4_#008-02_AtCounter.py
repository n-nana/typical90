# 008 - AtCounter（★4）
# 1次元配列DP ver.

MOD = 10**9 + 7

N = int(input())
S = input()

A = "atcoder"
M = len(A)

dp = [0]*(M+1)
dp[0] = 1

for i in range(N):
    for j in range(M):
        if S[i] == A[j]:
            dp[j+1] += dp[j]
            dp[j+1] %= MOD

print(dp[-1])

