#### 예제 입력이랑 반례는 맞는데 시간초과,,,,,,,, 

dx = [0, 1, 1]  # 우 하 우하
dy = [1, 0, 1]
# d가 3이면 nx, ny 기준 [-1, 0], [0, -1]도 0이어야 함
pd = [[0, 2], [1, 2], [0, 1, 2]]

def dfs(x, y, direc):
    global result
    if x == N-1 and y == N-1:   # 도착하면 result += 1
        result += 1
        return

    for d in pd[direc]:     # d(현재 방향)에 대해 갈 수 있는 방향들에 대해서
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            if arr[nx][ny] != 1:    # 범위 내에서 간 적 없고 해당 위치가 벽이 아니면 방문표시(2)하고 재귀 호출
                if d == 2:          # 만약 대각선이면
                    if arr[nx-1][ny] == 1 or arr[nx][ny-1] == 1:  # 두 칸 더 탐색해서 하나라도 1이 있으면 continue
                        continue
                visited[nx][ny] = 2
                dfs(nx, ny, d)
                visited[nx][ny] = 0
            # else:                 # else일 떼 return하면 안 됨,,, 다른 방향 탐색해야지,,
            #     return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
visited[0][0] = 2
visited[0][1] = 2
result = 0

dfs(0, 1, 0)
print(result)
