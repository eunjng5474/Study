import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
# arr = [[[0, 0, 0, 0, 0] for i in range(N)] for _ in range(N)]
arr = [[[] for _ in range(N)] for _ in range(N)]

# 질량, 속력, 방향, 이동 여부
for m in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

while K:
    K -= 1
    # 이동할 때 마다 새로운 배열 생성해서 집어넣기
    # 기존 배열에 저장하면 이동 전의 값과 이동 후에 값이 겹치면 중복으로 인식할 수 있음
    # 따라서 매번 이동한 위치 저장할 board 생성
    board = [[[] for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not arr[x][y]:
                continue

            for k in arr[x][y]:
                if not k[0]:
                    continue
                # 굳이 범위 초과할 때도 조건 안 주고 처음부터 % 사용해도 됨
                nx = (x + dx[k[2]] * k[1]) % N
                ny = (y + dy[k[2]] * k[1]) % N

                board[nx][ny].append([k[0], k[1], k[2]])

    for i in range(N):
        for j in range(N):
            if len(board[i][j]) >= 2:   # 합쳐질 때
                mm, ss = 0, 0
                dd = 1
                ll = len(board[i][j])
                odd_cnt = 0
                even_cnt = 0
                for p in board[i][j]:   # 모든 값들의 질량, 속력은 + 하고, 방향 탐색 위해 방향의 홀짝 여부 구하기
                    mm += p[0]
                    ss += p[1]
                    if p[2] % 2:
                        odd_cnt += 1
                    else:
                        even_cnt += 1

                # 다 홀수거나 짝수면 dd = 0으로 해서 이후 0, 2, 4, 6으로 되도록
                # 아닌 경우 dd = 1이니까 1, 3, 5, 7이 됨
                if odd_cnt == ll or even_cnt == ll:
                    dd = 0

                board[i][j] = []
                for d in range(4):      # 여기서 dd + 2*d
                    board[i][j].append([mm//5, ss//ll, dd+2*d])

    # board에만 바뀐 값 저장되어 있으므로 arr에 저장하기
    for i in range(N):
        for j in range(N):
            arr[i][j] = board[i][j]


result = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            for k in arr[i][j]:
                result += k[0]

print(result)













    #         if arr[x][y]:   # 값 있고 이동 안 했으면
    #             for k in range(len(arr[x][y])):
    #                 if arr[x][y][k][0] == 0:
    #                     arr[x][y].pop(k)
    #                 if not arr[x][y][k][3] and arr[x][y][k][0]:
    #
    #                     nx = x + dx[arr[x][y][k][2]] * arr[x][y][k][1]
    #                     ny = y + dy[arr[x][y][k][2]] * arr[x][y][k][1]
    #
    #                     if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 음수여도 알아서 처리됨
    #                         nx = nx % N
    #                         ny = ny % N
    #
    #                     # (nx, ny)에 중복되면 이후 나누기 위해 dup에 해당 좌표 저장
    #                     # if arr[nx][ny]:
    #                     #     if (nx, ny) not in dup:
    #                     #         dup.append((nx, ny))
    #
    #                     arr[x][y][k][3] = 1             # 이동했다는 표시
    #                     arr[nx][ny].append(arr[x][y][k])    # (nx, ny)에 이전 위치의 값(이동 여부만 1로 바꿈) 저장
    #             arr[x][y] = []  # arr[x][y]에 있는 개수만큼 다 돌았으면 arr[x][y] 초기화
    #
    # # for a in arr:
    # #     print(a)
    # # print()
    # # print()
    # #
    # # print(dup)
    # for i in range(N):
    #     for j in range(N):
    #         if arr[i][j]:
    #             mm = 0
    #             ss = 0
    #             dd = 0
    #             n = 0
    #             for l in range(len(arr[i][j])):
    #                 mm += arr[i][j][l][0]
    #                 ss += arr[i][j][l][1]
    #                 n += 1
    #
    #                 if l > 0:
    #                     if arr[i][j][l][2] % 2 != arr[i][j][l-1][2] % 2:
    #                         dd = 1
    #
    #             arr[i][j] = []
    #             for k in range(4):
    #                 d4 = dd + k*2
    #
    #                 arr[i][j].append([mm//5, ss//n, d4, 0])
    #
    # for a in range(N):
    #     for b in range(N):
    #         if arr[a][b]:
    #             arr[a][b][0][3] = 0
    #
    # for a in arr:
    #     print(a)
    # print()

# result = 0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j]:
#             for k in range(len(arr[i][j])):
#                 result += arr[i][j][k][0]
#
# print(result)





#
# while K:
#     K -= 1
#     dup = []    # 합쳐지는 곳의 x, y좌표 저장
#     for x in range(N):
#         for y in range(N):
#
#             if arr[x][y][0] and not arr[x][y][4]:    # 개수 있으면
#                 # print('x, y: ', x, y)
#
#                 if not arr[x][y][1]:            # 질량 0인 경우 초기화
#                     arr[x][y] = [0, 0, 0, 0, 0]
#
#                 nx = x + dx[arr[x][y][3]] * arr[x][y][2]
#                 ny = y + dy[arr[x][y][3]] * arr[x][y][2]
#
#                 if nx < 0 or nx >= N or ny < 0 or ny >= N:  # 음수여도 알아서 처리됨
#                     nx = nx % N
#                     ny = ny % N
#
#                 # if nx < 0:
#                 #     nx = N - (-nx % N)
#                 # if ny < 0:
#                 #     ny = N - (-ny % N)
#                 # # if nx < 0 or ny < 0:        # 범위 벗어날 때
#                 # #     nx = N + (nx % N) + 1
#                 # #     ny = N + (ny % N) + 1
#                 # if nx >= N or ny >= N:
#                 #     nx = nx % N
#                 #     ny = ny % N
#
#                 # print('nx, ny: ', nx, ny)
#                 if arr[nx][ny][0]:      # 그 자리에 이미 있을 때
#                     arr[nx][ny][0] += 1
#                     arr[nx][ny][1] += arr[x][y][1]
#                     # arr[nx][ny][2] += arr[x][y][2]
#                     arr[nx][ny][2] += arr[x][y][2]
#                     if arr[nx][ny][3] % 2 == arr[x][y][3] % 2:      # 방향 홀/짝 동일
#                         arr[nx][ny][3] = 0
#                     else:                       # 비동일
#                         arr[nx][ny][3] = 1
#
#                     if (nx, ny) not in dup:
#                         dup.append((nx, ny))
#
#                 else:
#                     arr[nx][ny] = arr[x][y]     # 이동 후 원래 자리 초기화
#                 arr[nx][ny][4] = 1
#                 arr[x][y] = [0, 0, 0, 0, 0]
#
#     # print('dup: ', dup)
#     # for a in arr:
#     #     print(a)
#     # print()
#     # print()
#
#     # for i in range(len(dup)):
#     #     for j in range(len(dup)):
#     if dup:
#         for i, j in dup:
#                 # if arr[nx][ny][2] == 0:
#             for k in range(4):
#                 d = arr[i][j][3] + k*2
#
#                 ni = i + dx[d]
#                 nj = j + dy[d]
#
#                 if nx < 0 or nx >= N or ny < 0 or ny >= N:
#                     nx = nx % N
#                     ny = ny % N
#
#                 # 나눠지기만 하고 바로 이동 안 함,,,,,,,,, 수정하자
#                 arr[ni][nj][0] = 1
#                 arr[ni][nj][1] = arr[i][j][1]//5
#                 arr[ni][nj][2] = arr[i][j][2]//arr[i][j][0]
#                 arr[ni][nj][3] = d
#                 arr[ni][nj][4] = 0
#             arr[i][j] = [0, 0, 0, 0, 0]
#
#
#     for a in arr:
#         print(a)
#     print()
#
#
#
