import sys
sys.stdin = open('input1.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    global result
    cnt = arr[x][y]
    num = arr[x][y]
    for d in range(4):
        for n in range(1, num+1):
            nx = x + dx[d] * n
            ny = y + dy[d] * n

            if 0 <= nx < N and 0 <= ny < M:
                cnt += arr[nx][ny]
    if cnt > result:
        result = cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(M):
            search(i, j)

    print(f'#{tc} {result}')
