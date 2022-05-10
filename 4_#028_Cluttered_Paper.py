#028 - Cluttered Paper（★4）
# 2次元いもす法

N = int(input())
K = 1010 # 範囲外アクセス回避のため+10
res = [[0]*K for _ in range(K)] # 入力データ格納
cs = [[0]*K for _ in range(K)] # cumsum: 累積和

for _ in range(N):
    lx,ly,rx,ry = map(int,input().split())
    res[ly][lx] += 1
    res[ry][rx] += 1
    res[ry][lx] -= 1
    res[ly][rx] -= 1

# 横方向に積算
for y in range(K):
    for x in range(K):
        if x == 0:
            cs[y][x] = res[y][x]
        else:
            cs[y][x] = cs[y][x-1] + res[y][x]

# 縦方向に積算
for y in range(K):
    for x in range(K):
        if y == 0:
            cs[y][x] = cs[y][x]
        else:
            cs[y][x] = cs[y-1][x] + cs[y][x]

# 数え上げ
ans = [0]*(N+1)
for y in range(K):
    for x in range(K):
        p = cs[y][x]
        ans[p] += 1

for i in range(1,N+1):
    print(ans[i])
    
#print(*res,sep="\n")
#print()
#print(*cs,sep="\n")



