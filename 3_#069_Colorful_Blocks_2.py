#069 - Colorful Blocks 2（★3）

MOD = 10**9 + 7

N,K = map(int,input().split())
if N == 1:
    ans = K%MOD
elif N == 2:
    ans = K*(K-1)%MOD
else:
    ans = K*(K-1)*pow(K-2,N-2,MOD)%MOD

print(ans)

