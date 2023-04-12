import sys
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global shark
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    possible = []

    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] <= shark and not visited[nx][ny]: # 이동 가능하면
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

                    if 0 < arr[nx][ny] < shark:     # 먹을 수 있으면
                        possible.append([visited[nx][ny]-1, nx, ny])  # 가능한 리스트에 추가

    possible.sort(key=lambda x:(x[0], x[1], x[2]))  # 거리-행-열 순으로 정렬
    return possible



N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = 2
cnt = 0
time = 0
# fishes = [[] for _ in range(N*N)]

# fish = 0
# flag = False
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            x, y = i, j     # 상어 위치 저장하고 0으로 바꿔서 추후에 갈 수 있도록
            arr[i][j] = 0
        # if arr[i][j] and arr[i][j] != 9:
        #     fish += 1


while True:
    visited = [[0] * N for _ in range(N)]
    lst = bfs(x, y)

    if not lst:     # 갈 수 있는 곳 없으면 종료
        break

    dist, x, y = lst[0]
    cnt += 1            # 갈 수 있는 리스트 중 첫번째에 가서 물고기 먹기
    # shark += 1
    time += dist        # 거리만큼 시간 소요

    if shark == cnt:    # 먹은 물고기 수 == 상어 크기이면 상어 크기 증가하고, cnt 초기화
        shark += 1
        cnt = 0

    arr[x][y] = 0       # 먹은 곳 0으로 바꾸기

print(time)






#
# def dfs(x, y, cnt, shark, time):
#     if cnt == fish:
#         print('time: ', time)
#         return
#
#     if not arr[x][y] and arr[x][y] < shark:
#         arr[x][y] = 0
#
#     possible = []
#     for i in range(shark):
#         for j in range(len(fishes[i])):
#             nx = fishes[i][j][0]
#             ny = fishes[i][j][1]
#             dist = abs(nx-x) + abs(ny-y)
#             possible.append([dist, nx, ny])
#
#     possible.sort(key=lambda x:(x[0], x[1], x[2]))
#     # print()
#     # print(possible)
#     # print()
#     xx = possible[0][1]
#     yy = possible[0][2]
#     distance = possible[0][0]
#
#     dfs(xx, yy, cnt+1, shark+1, time+distance)

