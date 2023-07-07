# 086 - Snuke's Favorite Arrays（★5）
# https://zenn.dev/m193h/articles/c9495557d135a4

MOD = 1000000007
MOD = 10**9 + 7
N,Q = map(int,input().split())

P = []
for _ in range(Q):
    x,y,z,w = map(int,input().split())
    x -= 1
    y -= 1
    z -= 1
    P.append((x,y,z,w))

pro = 1
for d in range(60): #***********************
    B = [True]*(1<<N)
    for i in range(1<<N):
        A = []
        for j in range(N):
            if (i>>j)&1 == 1:
                A.append(1)
            else:
                A.append(0)
        
        for x,y,z,w in P:
            if (w>>d)&1 != (A[x]|A[y]|A[z]):
                B[i] = False

    pro *= B.count(True)
    pro %= MOD
    
print(pro)
        
    
    
