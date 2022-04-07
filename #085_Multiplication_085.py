# 085 - Multiplication 085（★4）
# 約数列挙？をつかった方法だともっと早くできそう（そのうち、、）

K = int(input())
N1 = int(pow(K,(1/3))//1) + 2

ans = 0
for a in range(1,N1):
    # bの探索範囲を減らした
    N2 = int(pow(K/a,(1/2))//1) + 2
    for b in range(a,N2):
        c = K/a/b
        if c < b:
            continue
        if c < 1:
            break
        if c.is_integer():
            ans += 1
print(ans)




