import copy

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    tmp_arr[x][y] = 1
    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0<= nx < N and 0 <= ny < N:
            if tmp_arr[nx][ny] != 1 and tmp_arr[nx][ny] != 0:
                DFS(nx, ny)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

min_n = arr[0][0]
max_n = arr[0][0]

result = []

for a in arr:
    if max(a) > max_n:
        max_n = max(a)
    if min(a) < min_n:
        min_n = min(a)

for n in range(min_n, max_n+1):
    tmp_arr = copy.deepcopy(arr)
    for i in range(N):
        for j in range(N):
            if tmp_arr[i][j] <= min_n:
                tmp_arr[i][j] = 0

    print()
    for t in tmp_arr:
        print(t)
    print()

    cnt = 0
    for x in range(N):
        for y in range(N):
            if tmp_arr[x][y] != 0:
                cnt += 1
                DFS(x, y)
    result.append(cnt)

print(result)
    
