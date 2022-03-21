#064 - Uplift（★3）

N,Q = map(int, input().split())
A = list(map(int, input().split()))

H = [] # 標高差（階差）
res = 0
for i in range(1,N):
    diff = A[i] - A[i-1]
    H.append(diff)
    res += abs(diff)
    
for _ in range(Q):
    l,r,v = map(int, input().split())
    
    # 西端が含まれる場合（l=1）は計算しない
    if l > 1:
        l -= 2 # indexの補正（1-index + 階差計算分で-2）
        res -= abs(H[l]) # 変動前の標高差を引く
        H[l] += v # 標高差の更新
        res += abs(H[l]) # 変動後の標高差を足す
        
    # 東端が含まれる場合（r=N）は計算しない
    if r < N:
        r -= 2
        res -= abs(H[r+1]) # 変化するのはr+1の位置
        H[r+1] -= v
        res += abs(H[r+1]) # 変化するのはr+1の位置
        
    print(res)

