dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def search(x, y):
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]



N = int(input())
arr = [map(int, input().split()) for _ in range(N)]
result = 0

for i in range(N):
    for j in range(N):
        search(i, j)