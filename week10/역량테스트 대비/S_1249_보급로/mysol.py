import sys
sys.stdin = open('input.txt')
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global result
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny]:
                    if visited[nx][ny] > visited[x][y] + arr[nx][ny]:
                        visited[nx][ny] = visited[x][y] + arr[nx][ny]
                    else:
                        continue
                else:
                    visited[nx][ny] = visited[x][y] + arr[nx][ny]
                q.append((nx, ny))




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    result = 100*100*10
    bfs(0, 0)
    print(f'#{tc} {visited[N-1][N-1]-1}')