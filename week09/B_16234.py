import sys
input = sys.stdin.readline
from collections import deque


dx = [0, 1, 0, -1] # 우하좌상
dy = [1, 0, -1, 0]

def bfs(x, y, num):
    global flag, xy_lst
    q = deque()
    q.append((x, y))
    visited[x][y] = num

    tmp_set = set()
    tmp_set.add((x, y))
    tmp_sum = arr[x][y]
    while q:
        x, y = q.popleft()

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                    flag = True
                    visited[nx][ny] = num
                    q.append((nx, ny))
                    tmp_set.add((nx, ny))
                    tmp_sum += arr[nx][ny]

    xy_lst.append([tmp_sum, tmp_set])





N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
while True:
    visited = [[0] * N for _ in range(N)]

    xy_lst = []
    num = 0
    flag = False
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                num += 1
                bfs(i, j, num)

    if not flag:
        print(cnt)
        break

    cnt += 1
    for l in xy_lst:
        people = l[0] // len(l[1])
        for x, y in l[1]:
            arr[x][y] = people




#### 시간초과
    # for n in range(1, num+1):
    #     sum_n = 0
    #     cnt_n = 0
    #     lst = []
    #     for a in range(N):
    #         for b in range(N):
    #             if visited[a][b] == n:
    #                 sum_n += arr[a][b]
    #                 cnt_n += 1
    #                 lst.append((a, b))
    #
    #     if cnt_n >= 2:
    #         for l in lst:
    #             arr[l[0]][l[1]] = sum_n // cnt_n











# def sol(x, y):
#     for d in range(2):
#         nx = x + dx[d]
#         ny = y + dy[d]
#
#         if 0 <= nx < N and 0 <= ny < N:
#             if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
#                 lst.add((x, y))
#                 lst.add((nx, ny))



#
#
# N, L, R = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
#
# cnt = 0
#
# while True:
#     lst = []
#     # tmp = 0
#     # if not tmp:
#     #     union = set()
#     union = set()
#     for x in range(N):
#         for y in range(N):
#             tmp = 0
#             for d in range(2):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
#
#                 if 0 <= nx < N and 0 <= ny < N:
#                     if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
#                         union.add((x, y, arr[x][y]))
#                         union.add((nx, ny, arr[nx][ny]))
#                     else:
#                         tmp += 1
#             if tmp == 2:
#                 lst.append(union)
#                 tmp = 0
#                 union = set()
#     if x == N-1 and y == N-1:
#         lst.append(union)
#
#
#     if not lst:
#         break
#     cnt += 1
#
#     for l in lst:
#         print(l)
#     print()
#
#     for l in lst:
#         sum_n = 0
#         for j in l:
#             sum_n += j[2]
#         num = sum_n // len(l)
#
#         for k in l:
#             arr[k[0]][k[1]] = num
#
#     # for a in arr:
#     #     print(a)
#     # print()
#
# print(cnt)