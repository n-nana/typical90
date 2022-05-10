#052 - Dice Product（★3）

N = int(input())
MOD = 10**9 + 7

ans = 1
for i in range(N):
    A = list(map(int, input().split()))
    ans *= sum(A)
    ans %= MOD

print(ans)

