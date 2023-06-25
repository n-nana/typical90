#066 - Various Arrays（★5）
#期待値の線形性

N = int(input())

A = []
for _ in range(N):
    L,R = map(int,input().split())
    A.append([L,R])

E = 0
for i in range(N-1):
    for j in range(i+1, N):
        Li, Ri = A[i]
        Lj, Rj = A[j]
        bottom = (Ri - Li + 1)*(Rj - Lj + 1)
        top = 0
        for Vi in range(Li, Ri+1):
            if Rj < Vi:
                c = Rj - Lj + 1
            elif Lj < Vi <= Rj:
                c = Vi - Lj
            elif Vi <= Lj:
                c = 0
            top += c
        E += top/bottom

print(E)
        
