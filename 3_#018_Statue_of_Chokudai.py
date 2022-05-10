#018 - Statue of Chokudai（★3）

import math

T = int(input())
L,X,Y = map(int, input().split())
x = 0

Q = int(input())
for _ in range(Q):
    E = int(input())
    E %= T
    ang = 2*math.pi*E/T # E分後の観覧車の角度
    
    # y: 観覧車のy座標, x: x座標, r: 観覧車と銅像の平面距離
    y = (L/2)*(-1)*math.sin(ang)
    z = (L/2)*(-1)*math.cos(ang) + L/2
    r = pow((Y-y)**2 + (X-x)**2, 0.5)
    
    # atan2関数というのもあるっぽい
    rad = math.atan(z/r)
    deg = math.degrees(rad)
    #print(deg)
    print('{:.8f}'.format(deg)) # 絶対誤差が10**(-7)なので8f指定している
