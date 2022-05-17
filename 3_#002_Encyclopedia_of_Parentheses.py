# 002 - Encyclopedia of Parentheses（★3）
# bit全探索, 正しいカッコ列の条件

import itertools

N = int(input())

ans = []
for P in itertools.product([0,1],repeat = N):

    # 正しいカッコ列の条件
    # 01. "(" と ")" の数が等しい
    # 02. 全ての範囲で "(" の数が ")" の数以上
    
    diff = 0
    for p in P:
        if p == 0: diff += 1
        else: diff -= 1
        if diff < 0: # 条件2を満たさない場合
            break
            
    if diff == 0: # 条件1を満たす場合
        tmp = []
        for p in P:
            if p == 0: tmp.append("(")
            else: tmp.append(")")
        tmp = "".join(tmp)
        ans.append(tmp)
        
print(*ans,sep="\n")
        
