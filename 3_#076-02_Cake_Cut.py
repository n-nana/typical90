# 076 - Cake Cut（★3）
# 累積和 + 2分探索 ver.

from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int,input().split()))
W = sum(A)

A += A
ans = "No"

# CumSum
cs = [0]
for a in A:
    nxt = cs[-1] + a
    cs.append(nxt)

#print(cs)

for i in range(2*N):
    a = cs[i]
    diff = a - W/10
    if diff < 0:
        continue
    j = bisect_left(cs,diff)
    b = cs[j]
#    print(a,b,diff,W/10)
    if abs(a - b) == W/10:
        ans = "Yes"
    
print(ans)


