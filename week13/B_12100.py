N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

def sol(cnt):
    global result

    if cnt == 0:
        for i in range(N):
            result = max(result, max(arr[i]))
        return

    for d in range(4):
        visited = [[0] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                if arr[x][y]:
                    while True:
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if visited[nx][ny]:
                            continue

                        if arr[nx][ny]:
                            arr[nx][ny] += arr[x][y]
                            arr[x][y] = 0
                            visited[nx][ny] = 1
                            break
                        elif nx == 0 or ny == 0 or nx == N-1 or ny == N-1:
                            arr[nx][ny] = arr[x][y]
                            arr[x][y] = 0
                            visited[nx][ny] = 1
                            break
                        else:
                            x, y = nx, ny



    # for x in range(N):
    #     for y in range(N):
    #         if arr[x]
    #         for n in range(N):
    #             for d in range(4):
    #                 nx = x + dx[d] * n
    #                 ny = y + dy[d] * n
    #
    #                 if 0 <= nx < N and 0 <= ny < N:
    #                     if arr[nx][ny] and arr[nx][ny] == arr[x][y]:
    #                         tmp = arr[x][y]
    #                         arr[nx][ny] += tmp
    #                         arr[x][y] = 0
    #                         sol(nx, ny, cnt-1)
    #                         arr[x][y] = tmp
    #
    #                     else:
    #                         if nx == x or ny == y:
    #                             tmp = arr[x][y]
    #                             arr[nx][ny] = tmp
    #                             sol(nx, ny)
    #

# for i in range(N):
#     for j in range(N):
#         if arr[i][j]:

print(result)