N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

def move(d):
    moved = [[0] * N for _ in range(N)]
    # 두 번 움직이지 않도록 새로운 배열 생성
    ## 위로 이동
    if d == 0:
        # 첫 줄은 arr의 첫줄 그대로 가져오기
        moved[0] = list(arr[0])
        # 자기 위 값과 비교해서 같은 숫자면 위 숫자에 더해짐
        for x in range(1, N):
            for y in range(N):
                if arr[x][y]:
                    if arr[x-1][y] == arr[x][y]:
                        moved[x-1][y] *= 2
                        arr[x][y] = 0
                    else:
                        moved[x][y] = arr[x][y]
        # 더해지고 난 뒤 모든 값 가장 위로 올리기
        for p in range(1, N):
            for q in range(N):
                i, j = p, q
                if moved[i][j]:
                    while i >= 0:
                        if not moved[i-1][j]:
                            moved[i-1][j] = moved[i][j]
                            moved[i][j] = 0
                        else:
                            break
                        i -= 1

    # 아래로 이동
    elif d == 1:
        moved[N-1] = list(arr[N-1])
        for x in range(N-2, -1, -1):
            for y in range(N):
                if arr[x][y]:
                    if arr[x+1][y] == arr[x][y]:
                        moved[x+1][y] *= 2
                        arr[x][y] = 0
                    else:
                        moved[x][y] = arr[x][y]

        for p in range(N-2, -1, -1):
            for q in range(N):
                i, j = p, q
                if moved[i][j]:
                    while i < N-1:
                        if not moved[i+1][j]:
                            moved[i+1][j] = moved[i][j]
                            moved[i][j] = 0
                        else:
                            break
                        i += 1

    # 왼쪽으로
    elif d == 2:
        # 0열 가져오기
        for x in range(N):
            moved[x][0] = arr[x][0]
            for y in range(1, N):
                if arr[x][y]:
                    if arr[x][y-1] == arr[x][y]:
                        moved[x][y-1] *= 2
                        arr[x][y] = 0
                    else:
                        moved[x][y] = arr[x][y]

        for p in range(N):
            for q in range(1, N):
                i, j = p, q
                if moved[i][j]:
                    while j >= 0:
                        if not moved[i][j-1]:
                            moved[i][j-1] = moved[i][j]
                            moved[i][j] = 0
                        else:
                            break
                        j -= 1

    # 오른쪽으로





#     for m in moved:
#         print(m)
#     print()
#
# move(2)
















#
# def sol(cnt, d):
#     global result
#
#     if cnt == 0:
#         for i in range(N):
#             result = max(result, max(arr[i]))
#         return
#
#     # for d in range(4):
#     visited = [[0] * N for _ in range(N)]
#     for x in range(N):
#         for y in range(N):
#             if arr[x][y]:
#                 while True:
#                     nx = x + dx[d]
#                     ny = y + dy[d]
#                     if visited[nx][ny]:
#                         continue
#
#                     if arr[nx][ny]:
#                         arr[nx][ny] += arr[x][y]
#                         arr[x][y] = 0
#                         visited[nx][ny] = 1
#                         break
#                     elif nx == 0 or ny == 0 or nx == N-1 or ny == N-1:
#                         arr[nx][ny] = arr[x][y]
#                         arr[x][y] = 0
#                         visited[nx][ny] = 1
#                         break
#                     else:
#                         x, y = nx, ny
#
#     sol(cnt-1, 0)
#     sol(cnt-1, 1)
#     sol(cnt-1, 2)
#     sol(cnt-1, 3)
#
#
# sol(5, 0)
# sol(5, 1)
# sol(5, 2)
# sol(5, 3)



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

# print(result)