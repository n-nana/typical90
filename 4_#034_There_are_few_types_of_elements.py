#034 - There are few types of elements（★4）
#deque尺取り法

from collections import deque

N,K = map(int,input().split())
A = list(map(int,input().split()))

dct = dict() # 要素の種類数（&個数）を管理
deq = deque()
ans = 0
for a in A:
    
    # 右側に要素を追加(append)
    deq.append(a)
    if a not in dct:
        dct[a] = 1
    else:
        dct[a] += 1
    
    # （要素がK種類を超えていれば）左側の要素を削除(popleft)
    while len(deq) > 0 and len(dct) > K:
        r = deq.popleft()
        if dct[r] > 1:
            dct[r] -= 1
        else:
            del dct[r] # 辞書の値が0であればkeyを消す
            
#    print(dct,deq,len(dct))

    ans = max(len(deq), ans)
        
print(ans)

