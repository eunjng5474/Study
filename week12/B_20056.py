import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
arr = [[[0, 0, 0] for i in range(N+1)] for _ in range(N+1)]
for m in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r][c] = [m, s, d]

while K:
    K -= 1

