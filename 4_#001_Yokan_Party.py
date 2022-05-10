#001 - Yokan Party（★4）
# 最小値の最大化は二分探索

N,L = map(int, input().split())
K = int(input())
A = list(map(int, input().split()))

ok = -1 # K回以上分割して得られるスコア
ng = L+1 # 条件からは得られないスコア

while abs(ok-ng) > 1:
    mid = (ok+ng)//2
    cut = 0 # 切れ目の数
    l = 0 # ようかんの左端
    
    for r in A:
        if r-l >= mid:
            cut += 1 # ようかんがmid以上の長さなったら分割
            l = r # 左端を更新
    
    if cut > K: # 切れ目がKを越えていればスコアを得られる
        ok = mid
    elif cut < K: # K未満であればNG
        ng = mid
    else: # 切れ目がちょうどKの場合
        if L-l >= mid: # 最後のようかんの長さがmid以上
            ok = mid
        else: # mid未満
            ng = mid
        
print(ok)

