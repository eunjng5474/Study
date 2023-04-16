import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global result
    q = deque()
    tmp = 0
    cnt_0 = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:      # 1이면 q에 추가
                q.append((i, j))
            elif arr[i][j] == 0:    # 만약 시작 arr에 0이 없으면 탐색 안 해도 되기 때문에
                cnt_0 += 1          # 0의 개수 세기
    if cnt_0 == 0:                  # 만약 0이 없으면 result = 0으로 하고 return
        result = 0
        return

    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 0:
                    cnt = arr[x][y] + 1     # bfs라 이전 위치 + 1을 현재 위치로 저장할건데
                    arr[nx][ny] = cnt       # 마지막 위치 저장하기 위해 cnt라는 변수로 별도 저장
                    if cnt > tmp:           # 그래서 최대값인 cnt를 tmp로 저장
                        tmp = cnt
                    q.append((nx, ny))

    result = tmp - 1    # tmp는 가장 마지막 위치에 도달한 cnt인데 1부터 시작했으므로 result = cnt - 1



def check():                    # bfs 끝나고 0 있으면 result = -1이므로 확인
    global result
    tmp = 0
    for i in range(N):
        tmp += arr[i].count(0)
    if tmp:
        result = -1



M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 1000 * 1000
cnt = 0

bfs()
check()
print(result)