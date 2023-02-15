def DFS(start):
    visited[start] = 1
    stack = [start]
    pop_lst = []

    while stack:
        start = stack.pop()
        pop_lst.append(start)
        
        for next in range(1, N+1):
            if arr[start][next] == 1 and visited[next] == 0:
                stack.append(next)
            if next == N:
                return pop_lst 

    return pop_lst


N, M, R = map(int, input().split())
visited = [0] * (N+1)
arr = [[0] * (N+1) for _ in range(N+1)]
# cnt = 0

for n in range(N):
    u, v = map(int, input().split())
    arr[u][v] = 1
    arr[v][u] = 1

# print(arr)
print(DFS(R))
    

