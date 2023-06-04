#081 - Friendly Group（★5）
#二次元累積和

N,K = map(int,input().split())

mx = 5010
G = [[0]*mx for _ in range(mx)]

for _ in range(N):
    A,B = map(int,input().split())
    G[A][B] += 1

#横方向に累積和
for y in range(mx):
    for x in range(1,mx):
        G[y][x] += G[y][x-1]

#縦方向に累積和
for y in range(1,mx):
    for x in range(mx):
        G[y][x] += G[y-1][x]
        
res = 0
for ry in range(mx):
    for rx in range(mx):
        ly = max(0, ry-K-1) #y_min
        lx = max(0, rx-K-1) #x_min
        tmp = G[ry][rx] - G[ry][lx] - G[ly][rx] + G[ly][lx] #ry-K ~ ry, rx-K ~ rxの人数
        res = max(tmp, res)
        
print(res)
        
