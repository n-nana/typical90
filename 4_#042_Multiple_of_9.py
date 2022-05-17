#042 - Multiple of 9（★4）

N = 10**6 + 10
MOD = 10**9 + 7

#-------------------------
K = int(input())
dp = [0]*N
dp[0] = 1

for i in range(1,N):
    r = min(i,9)
    for j in range(1,r+1):
        dp[i] += dp[i-j]
        dp[i] %= MOD

print(dp[K] if K%9 == 0 else 0)

