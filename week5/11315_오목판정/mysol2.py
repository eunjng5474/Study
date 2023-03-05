import sys
sys.stdin = open('sample_input.txt')

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]

def search(i, j):
    global result
    x, y = i, j
    check = 0
    for d in range(8):
        cnt = 1
        while True:
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 'o':
                cnt += 1
                x, y = nx, ny
            else:
                break

            if cnt >= 5:
                result = 'YES'
                check = 1
                break
        if check:
            return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                search(i, j)

    print(f'#{tc} {result}')