# 085 - Multiplication 085（★4）
# 約数列挙ver.

K = int(input())

#--------------------------------
divisors = [] # Kの約数リスト
for i in range(1,K+1):
    if i*i > K: # これ以上は見ない
        break
    if K%i != 0: # 約数でないのでpass
        continue
    divisors.append(i)
    if i != K//i: # 商をリストに追加
        divisors.append(K//i)

divisors.sort()
#--------------------------------

N = len(divisors)
#print(divisors)

ans = 0
for i in range(N):
    a = divisors[i]
    for j in range(i,N):
        b = divisors[j]
        if (K//a)%b != 0: # a*bで割り切れないのでpass
            continue
        c = K//(a*b)
        if c < b:
            continue
        ans += 1

print(ans)
        
