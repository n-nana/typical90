# 030 - K Factors（★5）
# 計算量（N log log N）
# 素因数列挙
# 調和級数

N,K = map(int,input().split())

table = [0]*(N+3) # iの素因数の種類数

res = 0
for i in range(2, N+1):
    if table[i] == 0: # iが素数、
        for j in range(i, N+1, i):
            table[j] += 1 # iの倍数に+1
    if table[i] >= K:
        res += 1
        
print(res)
