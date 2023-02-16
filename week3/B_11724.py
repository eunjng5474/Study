

N, M = map(int, input().split())
arr = [[0] * (N+1) for _ in range(N+1)]
print(arr)

for m in range(M):
    u, v = map(int, input().split())
    arr[u][v] = 1
    arr[v][u] = 1

for i in range(N):
    for j in range(i+1, N+1):
        pass