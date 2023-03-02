import sys
sys.stdin = open('sample_input(1).txt')

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    md = N//2
    arr[md][md] = 2
    arr[md-1][md-1] = 2
    arr[md-1][md] = 1
    arr[md][md-1] = 1

    for m in range(M):
        a, b, c = map(int, input().split())
        x = a-1
        y = b-1
        arr[x][y] = c

        for d in range(8):
            nx = x + dx[d]
            ny = y + dy[d]
            stack = []

            while True:
                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    break

                if arr[nx][ny] != 0 and arr[nx][ny] != c:
                    stack.append((nx, ny))
                    nx = nx + dx[d]
                    ny = ny + dy[d]
                elif arr[nx][ny] == c:
                    for a, b in stack:
                        arr[a][b] = c
                    break
                elif arr[nx][ny] == 0:
                    break

    b_cnt = 0
    w_cnt = 0
    for a in arr:
        for b in a:
            if b == 1:
                b_cnt += 1
            if b == 2:
                w_cnt += 1

    print(f'#{tc} {b_cnt} {w_cnt}')


################

# for k in range(N):
#     for d in range(8):
#         nx = x + dx[d] * k
#         ny = y + dy[d] * k
#
#         if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == c:
#             for i in range(x, nx+1):
#                 for j in range(y, ny+1):
#                     if arr[i][j] != 0 and arr[i][j] != c:
#                         arr[i][j] = c
#                         break