# 029 - Long Bricks（★5）
# 区間変更・区間最大値取得
# https://atcoder.jp/contests/typical90/tasks/typical90_ac

#--------------------------------------------------
# ここに遅延評価セグメントツリーを貼る
#--------------------------------------------------    

#----------------------------------------------------------------
#INF = float("inf")

_id = 0 #恒等写像(lazy)
_e = 0 #単位元(data)

# 区間取得(値データどうしを合成)
def combine_node(x,y):
    return max(x,y)

# composition(遅延データを伝播), g（これまでの操作）, f（追加操作）
def combine_lazy(g,f):
    if f == _id:
        return g
    else:
        return f

# mapping(遅延データを値データに反映), xにfを作用させる
def reflect(x,f):
    if f == _id:
        return x
    else:
        return f

#----------------------------------------------------------------
W,N = map(int,input().split())

A = [0]*W
lst = LazySegmentTree(W, _e, _id, combine_node, combine_lazy, reflect)
lst.build(A)

for _ in range(N):
    L,R = map(int,input().split())
    L -= 1
    h = lst.fold(L,R)
    print(h+1)
    lst.update(L,R,h+1)
