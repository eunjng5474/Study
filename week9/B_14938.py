INF = int(1e9)

n, m, r = map(int, input().split())
items = [0] + list(map(int, input().split()))
# 2차원 리스트
graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신 -> 자기 자신은 0
for a in range(1, n+1):
    graph[a][a] = 0

for i in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l     # 양방향


# 기존 값과, i->k->j 중 최소값 저장
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 낙하지점에 따른 최대값 찾기
result = 0
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if graph[i][j] <= m:
            tmp += items[j]
    if tmp > result:
        result = tmp

print(result)
