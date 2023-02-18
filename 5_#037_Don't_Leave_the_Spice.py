#037 - Don't Leave the Spice（★5）
#解説はDPをセグメントツリーで高速化する方法（こっちは試していない、、

W,N = map(int,input().split())

#スパイス最小のDPテーブル
dp1 = [[-1]*(W+3) for _ in range(N+3)]
dp1[0][0] = 0

#スパイス最大のDPテーブル
dp2 = [[-1]*(W+3) for _ in range(N+3)]
dp2[0][0] = 0

res = -1
for i in range(N):
    L,R,V = map(int,input().split())
    for j in range(W,-1,-1):
        if dp1[i][j] != -1:
            if j+L <= W and W <= j+R:
                res = max(dp1[i][j]+V, res)
                
            dp1[i+1][j] = max(dp1[i][j], dp1[i+1][j])
            if j+L <= W:
                dp1[i+1][j+L] = max(dp1[i][j]+V, dp1[i+1][j+L])
            if j+R <= W:
                dp2[i+1][j+R] = max(dp1[i][j]+V, dp2[i+1][j+R])
                
        if dp2[i][j] != -1:
            if j+L <= W and W <= j+R:
                res = max(dp2[i][j]+V, res)
            
            dp2[i+1][j] = max(dp2[i][j], dp2[i+1][j])
            if j+L <= W:
                dp1[i+1][j+L] = max(dp2[i][j]+V, dp1[i+1][j+L])
            if j+R <= W:
                dp2[i+1][j+R] = max(dp2[i][j]+V, dp2[i+1][j+R])

print(res)
