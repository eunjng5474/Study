from heapq import heappop, heappush

def sol(n):
    visited[n[1]] = 0
    q = []
    heappush(q, n)
    while q:
        cost, now = heappop(q)
        if cost > visited[now]:
            continue
        for i in graph[now]:
            result = cost + i[0]
            if result < visited[i[1]]:
                visited[i[1]] = result
                heappush(q, (result, i[1]))

T = int(input())
for tc in range(1, T+1):
    N, M, s, e = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [int(1e9)] * (N+1)
    for m in range(M):
        u, v, w = map(int, input().split())
        graph[u].append((w, v))
        graph[v].append((w, u))

    sol((0, s))
    print(f'#{tc} {visited[e]}')