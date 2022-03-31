# 082 - Counting Numbers（★3）

def cnt(x):
    res = 0
    for i in range(1,n):
        l = 10**(i-1) # 桁内の最小値
        r = min(x, 10**i - 1) # 桁内の最大値 
        if r < l:
            break
        res += i*(r-l+1)*(l+r)//2
        res %= MOD

    return res

#-----------------------------
MOD = 10**9 + 7
L,R = map(int, input().split())
n = 20 # 10*18の桁（10**19 - 1）まで確認

ans = (cnt(R) - cnt(L-1))%MOD
print(ans)

