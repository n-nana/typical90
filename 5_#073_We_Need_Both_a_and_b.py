# 073 - We Need Both a and b（★5）
# 木DP、包除原理
# https://scrapbox.io/Example0911/競プロ典型90問_073_We_Need_Both_a_and_b(★5)

import sys
sys.setrecursionlimit(10**7)

def rec(crr,par):
    v1,v2 = 1,1
    for nxt in E[crr]:
        if nxt == par:
            continue
        rec(nxt,crr)
        
        if C[crr] == "a":
            v1 *= dp[nxt][0] + dp[nxt][2] # 分ける, 分けない
            v2 *= (dp[nxt][0] + dp[nxt][1] + dp[nxt][2]) + dp[nxt][2] # 分ける, 分けない    
        if C[crr] == "b":
            v1 *= dp[nxt][1] + dp[nxt][2]
            v2 *= (dp[nxt][0] + dp[nxt][1] + dp[nxt][2]) + dp[nxt][2]
        v1 %= MOD
        v2 %= MOD
        
    if C[crr] == "a":
        dp[crr][0] = v1
        dp[crr][2] = (v2 - v1)%MOD 
    if C[crr] == "b":
        dp[crr][1] = v1
        dp[crr][2] = (v2 - v1)%MOD

#------------------------------------        
MOD = 10**9 + 7
        
N = int(input())
C = input().split()

E = [[] for _ in range(N)]
for _ in range(N-1):
    a,b = map(int,input().split())
    E[a-1].append(b-1)
    E[b-1].append(a-1)

dp = [[0]*3 for _ in range(N)] # "a"のみ、"b"のみ、"a"と"b"
rec(0,-1)

ans = dp[0][2]
print(ans)
