# 048 - I will not drop out（★3）

N,K = map(int, input().split())

S = []
for _ in range(N):
    a,b = map(int, input().split())
    S.append(b)
    S.append(a-b)
S.sort(reverse=True)

cnt = 0
ans = 0
while cnt < K:
    ans += S[cnt]
    cnt += 1

print(ans)
