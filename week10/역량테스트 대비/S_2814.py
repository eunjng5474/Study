def sol(x, cnt):
    global result
    for i in graph[x]:
        if not visited[i]:
            visited[i] = 1
            sol(i, cnt+1)
            visited[i] = 0
    if cnt > result:
        result = cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for m in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    result = 0
    for n in range(1, N+1):
        visited[n] = 1
        sol(n, 1)
        visited[n] = 0
    print(f'#{tc} {result}')