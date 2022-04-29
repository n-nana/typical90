#058 - Original Calculator（★4）
#Doubling ver.

# 電卓の動作
def calc(x):
    z = x
    for dig in range(7):
        z += x%10
        x //= 10
    z %= MOD
    return z

#---------------------------------------    
N,K = map(int,input().split())

MOD = 10**5
#MOD = 30
gen = 60 # 2**60 ≒ 10**18
D = [[-1]*(MOD) for _ in range(gen+1)]

# 初期値（K=1の場合の遷移）
for j in range(MOD):
    D[0][j] = calc(j)

# K > 1の遷移
for i in range(gen):
    for j in range(MOD):
        D[i+1][j] = D[i][D[i][j]]

# 通った経路（表現、、）
move = []
for i in range(gen):
    if K>>i&1 == 1:
        move.append(i)
#print(move)

num = N
for p in move:
    num = D[p][num]
    
print(num)

