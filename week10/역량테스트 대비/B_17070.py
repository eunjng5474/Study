dx = [0, 1, 1]  # 우 하 우하
dy = [1, 0, 1]
# d가 3이면 nx, ny 기준 [-1, 0], [0, -1]도 0이어야 함
pd = [(0, 2), (1, 2), (0, 1, 2)]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
if arr[N-1][N-1]:
    print(result)
else:
    stack = []
    stack.append((0, 1, 0))
    arr[0][0] = 2
    arr[0][1] = 2
    while stack:
        x, y, direc = stack.pop()
        if x == N - 1 and y == N - 1:  # 도착하면 result += 1
            result += 1
            continue

        for d in pd[direc]:  # d(현재 방향)에 대해 갈 수 있는 방향들에 대해서
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if not arr[nx][ny]:  # 범위 내에서 간 적 없고 해당 위치가 벽이 아니면 방문표시(2)하고 재귀 호출
                    if d == 2:  # 만약 대각선이면
                        if arr[nx - 1][ny] == 1 or arr[nx][ny - 1] == 1:  # 두 칸 더 탐색해서 하나라도 1이 있으면 continue
                            continue
                    stack.append((nx, ny, d))
    print(result)



###### 재귀 쓰면 시간 초과
####### 그리고 리스트보다 튜플이 시간 더 짧음!!
#
# def dfs(x, y, direc):
#     global result
#     if x == N-1 and y == N-1:   # 도착하면 result += 1
#         result += 1
#         return
#
#     for d in pd[direc]:     # d(현재 방향)에 대해 갈 수 있는 방향들에 대해서
#         nx = x + dx[d]
#         ny = y + dy[d]
#
#         if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#             if arr[nx][ny] != 1:    # 범위 내에서 간 적 없고 해당 위치가 벽이 아니면 방문표시(2)하고 재귀 호출
#                 if d == 2:          # 만약 대각선이면
#                     if arr[nx-1][ny] == 1 or arr[nx][ny-1] == 1:  # 두 칸 더 탐색해서 하나라도 1이 있으면 continue
#                         continue
#                 visited[nx][ny] = 2
#                 dfs(nx, ny, d)
#                 visited[nx][ny] = 0
#             # else:                 # else일 떼 return하면 안 됨,,, 다른 방향 탐색해야지,,
#             #     return
