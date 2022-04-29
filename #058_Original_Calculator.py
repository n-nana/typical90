#058 - Original Calculator（★4）

# 電卓の動作
def calc(x):
    z = x
    for dig in range(7):
        z += x%10
        x //= 10
    z %= MOD
    return z

#---------------------------------------    
MOD = 10**5
INF = 10**5 + 10 # 適当に大きめの回数loopする用
N,K = map(int,input().split())

seen = [False]*MOD # 数字が表示されたかどうかを管理
num = [] # 数字が表示された順番
val = -1
for i in range(INF):
    if seen[N]: # すでに表示された数字が現れたら終了
        val = N
        break
    seen[N] = True
    num.append(N)
    N = calc(N)

a = num.index(val) # loopの最初の数字
b = seen.count(True) - 1 # loopの最後の数字

if K <= b:
    idx = K
else:
    idx = a + (K-a)%(b-a+1)

print(num[idx])

