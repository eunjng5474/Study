import sys
input = sys.stdin.readline
# from copy import deepcopy
from collections import deque

N, M, G, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ground = [[[0, 0] for _ in range(M)] for _ in range(M)]
for n in range(N):
    for m in range(M):
        if arr[n][m]:
            ground[n][m][0] = arr[n][m]

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 배양액 뿌리기
def baeyang(g_cnt, r_cnt):
    global result
    if g_cnt == 0 and r_cnt == 0:
        cnt = spread()
        result = max(result, cnt)
        return

    for n in range(N):
        for m in range(M):
            if arr[n][m] == 2 and not ground[n][m][0]:
                if g_cnt:
                    ground[n][m] = [1, 0]
                    baeyang(g_cnt-1, r_cnt)
                    ground[n][m] = [0, 0]
                if r_cnt:
                    ground[n][m] = [2, 0]
                    baeyang(g_cnt, r_cnt-1)
                    ground[n][m] = [0, 0]

# 퍼뜨리기
def spread():
    q = deque()
    flower_cnt = 0
    # q.append((x, y))
    for i in range(N):
        for j in range(M):
            if ground[i][j][0] == 1 or ground[i][j][0] == 2:
                q.append((i, j))
    while q:
        x, y = q.popleft()
        if ground[x][y][0] == 1 or ground[x][y][0] == 2:

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if nx < 0 or nx >= N or ny < 0 or ny >= M or not arr[nx][ny]:
                    continue
                # 배양액일 때 퍼뜨리기
                # if ground[nx][ny][0] == 1 or ground[nx][ny][0] == 2:
                if not ground[nx][ny][0]:
                    ground[nx][ny] = [ground[x][y][0], ground[x][y][1]+1]
                # 꽃 피우기
                elif ground[nx][ny][1] == ground[x][y][1]+1 and ground[nx][ny][0] != ground[x][y][0]:
                    ground[nx][ny] = [3, 0]
                    flower_cnt += 1
                    q.append((nx, ny))

    return flower_cnt


baeyang(G, R)
print(result)
# # 꽃 피우기
# def flower():
#     for x in range(N):
#         for y in range(M):
#             if


# def bfs(g_cnt, r_cnt, flower):
#     global result
#     if g_cnt == G and r_cnt == R:
#         result = max(flower, result)
#         return

    # for n in range(N):
    #     for m in range(M):

