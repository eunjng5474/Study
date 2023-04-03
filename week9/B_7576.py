import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(i, j, cnt):
    global result
    q = deque()
    q.append((i, j))
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1





M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 1000 * 1000