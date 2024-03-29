import sys
input = sys.stdin.readline
from copy import deepcopy
from collections import deque
from itertools import combinations


N, M, G, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# ground = [[[0, 0] for _ in range(M)] for _ in range(N)]
possible = []

for n in range(N):
    for m in range(M):
        # if arr[n][m]:
        #     ground[n][m][0] = arr[n][m]
        if arr[n][m] == 2:
            possible.append((n, m))

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(green_lst, red_lst):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    gq = deque()
    rq = deque()
    cnt = 0
    tmp = 1

    for g in green_lst:
        gq.append(g)
        visited[g[0]][g[1]] = -1

    for r in red_lst:
        rq.append(r)
        visited[r[0]][r[1]] = -1

    while gq and rq:
        for i in range(len(gq)):
        # while gq:
            gx, gy = gq.popleft()
            if visited[gx][gy] == int(1e9):
                continue

            for d in range(4):
                nx = gx + dx[d]
                ny = gy + dy[d]

                if nx < 0 or nx >= N or ny < 0 or ny >= M or not arr[nx][ny]:
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = tmp
                    gq.append((nx, ny))

        for j in range(len(rq)):
        # while rq:
            rx, ry = rq.popleft()
            if visited[rx][ry] == int(1e9):
                continue

            for d in range(4):
                nx = rx + dx[d]
                ny = ry + dy[d]

                if nx < 0 or nx >= N or ny < 0 or ny >= M or not arr[nx][ny]:
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = -1
                    rq.append((nx, ny))

                elif visited[nx][ny] == tmp:
                    cnt += 1
                    visited[nx][ny] = int(1e9)
        tmp += 1
    return cnt


for comb in combinations(possible, G+R):
    for green_lst in combinations(comb, G):
        red_lst = []
        for r in comb:
            if r not in green_lst:
                red_lst.append(r)
        result = max(result, bfs(green_lst, red_lst))

print(result)








# pos_set = set(possible)
# for green in combinations(possible, G):
#     rest = list(pos_set-set(green))
#     green_lst = list(green)
#     for red in combinations(rest, R):
#         red_lst = list(red)
#         result = max(result, bfs(green_lst, red_lst))
#
# print(result)




# # 퍼뜨리기
# def spread(ground):
#     q = deque()
#     flower_cnt = 0
#
#     for comb in combinations(possible, G_R):
#         for c in comb:
#             x, y = c[0], c[1]
#             q.append((x, y))
#
#     # q.append((x, y))
#     # for i in range(N):
#     #     for j in range(M):
#     #         if ground[i][j][0] == 1 or ground[i][j][0] == 2:
#     #             q.append((i, j))
#     while q:
#         x, y = q.popleft()
#         if ground[x][y][0] == 1 or ground[x][y][0] == 2:
#
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
#
#                 if nx < 0 or nx >= N or ny < 0 or ny >= M or not arr[nx][ny]:
#                     continue
#                 # 배양액일 때 퍼뜨리기
#                 # if ground[nx][ny][0] == 1 or ground[nx][ny][0] == 2:
#                 if not ground[nx][ny][0]:
#                     ground[nx][ny] = [ground[x][y][0], ground[x][y][1]+1]
#                 # 꽃 피우기
#                 elif ground[nx][ny][1] == ground[x][y][1]+1 and ground[nx][ny][0] != ground[x][y][0]:
#                     ground[nx][ny] = [3, 0]
#                     flower_cnt += 1
#                 q.append((nx, ny))
#
#     return flower_cnt
#
#
# # 배양액 뿌리기
# def baeyang(g_cnt, r_cnt):
#     global result
#     if g_cnt == 0 and r_cnt == 0:
#         cnt = spread(deepcopy(first_ground))
#         result = max(result, cnt)
#         return
#
#     for n in range(N):
#         for m in range(M):
#             if arr[n][m] == 2 and not ground[n][m][0]:
#                 if g_cnt:
#                     ground[n][m] = [1, 0]
#                     baeyang(g_cnt-1, r_cnt)
#                     ground[n][m] = [0, 0]
#                 if r_cnt:
#                     ground[n][m] = [2, 0]
#                     baeyang(g_cnt, r_cnt-1)
#                     ground[n][m] = [0, 0]
#
# # # 배양액 뿌리는 거 조합 사용
# # for comb in combinations(possible, G+R):
# #     for green in combinations(comb, G):
# #         map = deepcopy(first_ground)
# #         spread(map)
#
#
#
# # baeyang(G, R)
# print(result)
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


# for comb in combinations(possible, G+R):
#     # for c in comb:
#     print(comb)



# # 배양액 뿌리기
# def baeyang(g_cnt, r_cnt):
#     global result
#     if g_cnt == 0 and r_cnt == 0:
#         cnt = spread(deepcopy(first_ground))
#         result = max(result, cnt)
#         return
#
#     for n in range(N):
#         for m in range(M):
#             if arr[n][m] == 2 and not ground[n][m][0]:
#                 if g_cnt:
#                     ground[n][m] = [1, 0]
#                     baeyang(g_cnt-1, r_cnt)
#                     ground[n][m] = [0, 0]
#                 if r_cnt:
#                     ground[n][m] = [2, 0]
#                     baeyang(g_cnt, r_cnt-1)
#                     ground[n][m] = [0, 0]


# if nx < 0 or nx >= N or ny < 0 or ny >= M or not arr[nx][ny]:
#     continue
# # if 0 <= nx < N and 0 <= ny < M and arr[nx][ny]:
# if visited[nx][ny] == 0 and visited[nx][ny] < int(1e9):
#     if 0 < visited[x][y] < int(1e9):
#         visited[nx][ny] = visited[x][y] + 1
#     elif visited[x][y] < 0:
#         visited[nx][ny] = visited[x][y] - 1
#     q.append((nx, ny))
#
# if visited[nx][ny] + visited[x][y] + 1 == 0:
#     cnt += 1
#     visited[nx][ny] = int(1e9)
