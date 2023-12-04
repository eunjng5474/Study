import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

tetris=[[(0,0), (1,0), (0,1), (1,1)], # 정사각형
    [(0,0), (0,1), (0,2), (0,3)],  # 가로 직사각형
    [(0,0), (1,0), (2,0), (3,0)],  # 세로 직사각형
    [(0,0), (1,0), (2,0), (2,1)],  # 세로 긴 ㄴ
    [(0,1), (1,1), (2,1), (2,0)],  # 반대
    [(0,0), (0,1), (1,1), (2,1)],  # 세로 긴 ㄱ
    [(0,0), (0,1), (1,0), (2,0)],  # 반대
    [(0,0), (1,0), (1,1), (1,2)],  # 가로 긴 ㄴ
    [(1,0), (1,1), (1,2), (0,2)],  # 반대
    [(0,0), (0,1), (0,2), (1,2)],  # 가로 긴 ㄱ
    [(0,0), (0,1), (0,2), (1,0)],  # 반대
    [(0,1), (1,0), (1,1), (1,2)],  # ㅗ
    [(0,0), (0,1), (0,2), (1,1)],  # ㅜ
    [(0,0), (1,0), (1,1), (2,0)],  # ㅏ
    [(0,1), (1,1), (1,0), (2,1)],  # ㅓ
    [(0,0), (1,0), (1,1), (2,1)],
    [(0,1), (1,1), (1,0), (2,0)],
    [(1,0), (1,1), (0,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]]


def sol(x, y):
    global result
    for t in tetris:
        tmp = 0
        for d in t:
            nx = x + d[0]
            ny = y + d[1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            tmp += arr[nx][ny]
        result = max(result, tmp)

for x in range(N):
    for y in range(M):
        sol(x, y)

print(result)




#
# def square(x, y):      # 정사각형
#     global result
#
#     tmp = 0
#     for d in [(0, 0), (1, 0), (0, 1), (1, 1)]:
#         nx = x + d[0]
#         ny = y + d[1]
#
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             return
#         tmp += arr[nx][ny]
#
#     result = max(result, tmp)
#     return
#
# def bar(x, y):  # 직사각형
#     global result
#     tmp = 0
#     for d in [(0, 1), (1, 0)]:
#         for k in range(4):
#             nx = x + d[0] * k
#             ny = y + d[1] * k
#
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 return
#             tmp += arr[nx][ny]
#
#     result = max(result, tmp)
#     return
#
# def zigzag(x, y):       # 지그재그
#     global result
#     cnt1, tmp1, cnt2, tmp2 = 0, 0, 0, 0
#     for d in [(-1, 0), (0, 0), (0, 1), (1, 1)]:
#         nx = x + d[0]
#         ny = y + d[1]
#
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             continue
#         tmp1 += arr[nx][ny]
#         cnt1 += 1
#     if cnt1 == 4:
#         result = max(result, tmp1)
#
#     for dd in [(0, 0), (0, 1), (1, 0), (1, -1)]:
#         nnx = x + dd[0]
#         nny = y + dd[1]
#
#         if nnx < 0 or nnx >= N or nny < 0 or nny >= M:
#             continue
#         tmp2 += arr[nnx][nny]
#         cnt2 += 1
#     if cnt2 == 4:
#         result = max(result, tmp2)
#
#
# def other_col(x, y): # 나머지 두 도형 중 세로 방향
#     global result
#     tmp = 0
#     for d in [(-1, 0), (0, 0), (0, 1)]:
#         nx = x + d[0]
#         ny = y + d[1]
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             return
#         tmp += arr[nx][ny]
#
#     for dd in [(0, -1), (0, 1), (-1, -1), (1, 1)]:
#         nnx = x + dd[0]
#         nny = y + dd[1]
#         if nnx < 0 or nnx >= N or nny < 0 or nny >= M:
#             continue
#         result = max(result, tmp + arr[nnx][nny])
#
# def other_row(x, y):    # 가로
#     global result
#     tmp = 0
#     for d in [(0, -1), (0, 0), (0, 1)]:
#         nx = x + d[0]
#         ny = y + d[1]
#         if nx < 0 or nx >= N or ny < 0 or ny >= M:
#             return
#         tmp += arr[nx][ny]
#
#     for dd in [(-1, 0), (1, 0), (-1, 1), (1, -1)]:
#         nnx = x + dd[0]
#         nny = y + dd[1]
#         if nnx < 0 or nnx >= N or nny < 0 or nny >= M:
#             continue
#         result = max(result, tmp + arr[nnx][nny])
#
#
# for x in range(N):
#     for y in range(M):
#         square(x, y)
#         bar(x, y)
#         zigzag(x, y)
#         other_row(x, y)
#         other_col(x, y)
# print(result)