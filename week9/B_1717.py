import sys
input = sys.stdin.readline

## while 쓰면 시간초과

def find_set(x):
    if rep[x] == x:
        return x
    rep[x] = find_set(rep[x])
    # 이 과정에서 경로 압축이 되어서 시간 복잡도가 줄어든다고 한다..
    # 최악의 경우 시간 복잡도가 O(N)인데 경로압축 시 O(logN)
    # find_set을 통해 만난 모든 값의 부모 노드를 rep로
    return rep[x]

def union(x, y):
    rep[find_set(y)] = find_set(x)


n, m = map(int, input().split())
rep = [i for i in range(n+1)]
for tc in range(m):
    num, a, b = map(int, input().split())
    if num == 0:
        union(a, b)
    else:
        if find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")