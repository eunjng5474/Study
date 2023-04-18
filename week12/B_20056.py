import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
arr = [[[0, 0, 0, 0, 0] for i in range(N)] for _ in range(N)]
# 개수, 질량, 속력, 방향, 이동 여부
for m in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1] = [1, m, s, d, 0]

# for a in arr:
#     print(a)
# print()
# print()

while K:
    dup = []    # 합쳐지는 곳의 x, y좌표 저장
    for x in range(N):
        for y in range(N):

            if arr[x][y][0] and not arr[x][y][4]:    # 개수 있으면
                # print('x, y: ', x, y)

                if not arr[x][y][1]:            # 질량 0인 경우 초기화
                    arr[x][y] = [0, 0, 0, 0, 0]

                nx = x + dx[arr[x][y][3]] * arr[x][y][2]
                ny = y + dy[arr[x][y][3]] * arr[x][y][2]

                if nx < 0:
                    nx = N - (-nx % N)
                if ny < 0:
                    ny = N - (-ny % N)
                # if nx < 0 or ny < 0:        # 범위 벗어날 때
                #     nx = N + (nx % N) + 1
                #     ny = N + (ny % N) + 1
                if nx >= N or ny >= N:
                    nx = nx % N
                    ny = ny % N

                # print('nx, ny: ', nx, ny)
                if arr[nx][ny][0]:      # 그 자리에 이미 있을 때
                    arr[nx][ny][0] += 1
                    arr[nx][ny][1] += arr[x][y][1]
                    # arr[nx][ny][2] += arr[x][y][2]
                    arr[nx][ny][2] += arr[x][y][2]
                    if arr[nx][ny][3] % 2 == arr[x][y][3] % 2:      # 방향 홀/짝 동일
                        arr[nx][ny][3] = 0
                    else:                       # 비동일
                        arr[nx][ny][3] = 1

                    if (nx, ny) not in dup:
                        dup.append((nx, ny))

                else:
                    arr[nx][ny] = arr[x][y]     # 이동 후 원래 자리 초기화
                arr[nx][ny][4] = 1
                arr[x][y] = [0, 0, 0, 0, 0]

    # print('dup: ', dup)
    # for a in arr:
    #     print(a)
    # print()

    # for i in range(len(dup)):
    #     for j in range(len(dup)):
    if dup:
        for i, j in dup:
                # if arr[nx][ny][2] == 0:
            for k in range(4):
                d = arr[i][j][3] + k*2

                ni = i + dx[d]
                nj = j + dy[d]

                if ni < 0:
                    ni = N - (-ni % N)
                if nj < 0:
                    nj = N - (-nj % N)
                # if nx < 0 or ny < 0:        # 범위 벗어날 때
                #     nx = N + (nx % N) + 1
                #     ny = N + (ny % N) + 1
                if ni >= N or nj >= N:
                    ni = ni % N
                    nj = nj % N

                # if 0 <= ni < N+1 and 0 <= nj < N+1:
                arr[ni][nj][0] = 1
                arr[ni][nj][1] = arr[i][j][1]//5
                arr[ni][nj][2] = arr[i][j][2]//arr[i][j][0]
                arr[ni][nj][3] = d
                arr[ni][nj][4] = 0
            arr[i][j] = [0, 0, 0, 0, 0]

    K -= 1

    for a in arr:
        print(a)
    print()


