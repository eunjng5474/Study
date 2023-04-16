

n = int(input())
n1, n2 = map(int, input().split())
parent = [0] * (n+1)
child = [[] for _ in range(n+1)]

m = int(input())
for t in range(m):
    x, y = map(int, input().split())
    parent[y] = x
    child[x].append(y)

