import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 0 and visited[nx][ny] == 0:
            dfs(nx, ny)



N = int(input())
input_arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

max_height = 0
# min_height = 101
for i in range(N):                          # 최대 높이 구하기
    if max(input_arr[i]) > max_height:
        max_height = max(input_arr[i])
    # if min(input_arr[i]) < min_height:
    #     min_height = min(input_arr[i])

for m in range(max_height): # 0(아무 지역도 물에 잠기지 않을 수 있음) ~ 최대값 전까지
    cnt = 0
    arr = []
    for n in range(N):
        arr.append(list(input_arr[n]))  # input_arr 복제해서 새로 생성
    visited = [[0] * N for _ in range(N)]       # 방문 표시 초기화

    for i in range(N):
        for j in range(N):
            if arr[i][j] <= m:      # m보다 낮은 곳 0으로 바꾸기
                arr[i][j] = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0 and visited[i][j] == 0:   # 0 아니고 간 적 없으면 dfs 및 cnt += 1
                dfs(i, j)
                cnt += 1

    if cnt > result:
        result = cnt

print(result)
