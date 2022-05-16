#063 - Monochromatic Subgrid（★4）

from collections import defaultdict
from collections import Counter
import itertools

H,W = map(int,input().split())
G = []
for _ in range(H):
    g = list(map(int,input().split()))
    G.append(g)

ans = -1
for P in itertools.product([0,1],repeat = H): # it全探索
    flag = [] # bitが1であるH-index
    for i in range(H):
        if P[i] == 1:
            flag.append(i)
    
    if not flag: # 全て0の場合は対象なし
        tmp = 0
    else:
        dct = defaultdict(int)
        std = [] # 基準とする行（bitが1のものの内、最初の行）
        for x in range(W):
            std.append(G[flag[0]][x])
            
        for x in range(W): # 各列についてbitが1の行全てで値がstdと同じならok
            ok = True
            for y in flag:
                if G[y][x] != std[x]:
                    ok = False
            if ok:
                dct[std[x]] += 1
                
        if dct:
            dmax = max(dct.values())
            tmp = dmax*len(flag)
        else: # stdと一致する行・列がない
            tmp = 1
    ans = max(tmp,ans)
    
print(ans)
        



