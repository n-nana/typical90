#009 - Three Point Angle（★6）
# 中心を決めて２分探索、角度計算(atan2)

import math
import bisect

N = int(input())

P = []
for _ in range(N):
    x,y = map(int,input().split())
    P.append((x,y))
    
ans = 0
for j in range(N):
    jx,jy = P[j] # 中心の点(j)
    
    T = [] # 点(j)の座標を0,0に変換したときの、その他の点の角度
    for r in range(N):
        if r == j:
            continue
        rx,ry = P[r]
        rx,ry = rx - jx, ry - jy
        rt = math.degrees(math.atan2(ry, rx))%360
        T.append(rt)
    T.sort()
    
    # 点(i)を決めたときの、点(k)を2分探索で決める
    for i in range(N-1):
        it = T[i] # 点(i)の角度
        kt = (it + 180)%360 # 点(k)の角度の理想値(it + 180)

        #kt以上で最小のidx(=k未満である要素の個数)
        idx1 = min(len(T)-1, bisect.bisect_left(T, kt)) #(idx == len(T)の場合に注意)
        theta1 = max(it, T[idx1]) - min(it, T[idx1])
        theta1 = min(theta1, 360 - theta1)
        
        #kt以下で最大のidx
        idx2 = max(0, bisect.bisect_right(T, kt) - 1) #(idx == -1の場合に注意)
        theta2 = max(it, T[idx2]) - min(it, T[idx2])
        theta2 = min(theta2, 360 - theta2)
        
        ans = max(ans, theta1, theta2)
        
print(ans)
