import sys
input = sys.stdin.readline

w, h = map(int, input().split())
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
x, y = map(int, input().split())
result = 0

for i in range(N):
    if lst[i][0] == x:                  # 같은 방향일 때
        result += abs(lst[i][1] - y)
    elif [lst[i][0], x] in [[1, 2], [2, 1]]:    # (남-북)일 때
        d1 = y + lst[i][1]
        d2 = abs(w-y) + abs(w-lst[i][1])
        result += min(d1, d2)
        result += h
    elif [lst[i][0], x] in [[3, 4], [4, 3]]:    #(동-서)일 때
        d1 = y + lst[i][1]
        d2 = abs(h-y) + abs(h-lst[i][1])
        result += min(d1, d2)
        result += w

    else:           # (북-서)와 같이 코너를 중심으로 꺾여있을 때
        if x == 1:
            result += lst[i][1]
            if lst[i][0] == 3:
                result += y
            elif lst[i][0] == 4:
                result += (w-y)
        elif x == 2:
            result += (h - lst[i][1])
            if lst[i][0] == 3:
                result += y
            elif lst[i][0] == 4:
                result += (w-y)
        elif x == 3:
            result += lst[i][1]
            if lst[i][0] == 1:
                result += y
            elif lst[i][0] == 2:
                result += (h-y)
        elif x == 4:
            result += (w - lst[i][1])
            if lst[i][0] == 1:
                result += y
            elif lst[i][0] == 2:
                result += (h-y)

print(result)


































# import sys
# input = sys.stdin.readline
#
# # from collections import deque
#
# stack = []
# def dfs(x, y, n):
#     global result
#     cnt = 1
#     stack.append((x, y))
#     while stack:
#         x, y = stack.pop()
#         visited[x][y] = cnt
#         cnt += 1
#
#         for d in range(4):
#             nx = x + dx[d]
#             ny = y + dy[d]
#
#             if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != -1 and visited[nx][ny] == 0:
#                 stack.append((nx, ny))
#                 visited[nx][ny] = cnt
#
#                 if arr[nx][ny] == n:
#                     result += visited[nx][ny]
#                     break
#             else:
#                 pass
#
#         for v in visited:
#             print(v)
#         print()
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# w, h = map(int, input().split())
# arr = [[0] * w] + [[0] + [-1] * (w-2) + [0] for _ in range(h-1)] + [[0] * w]
# # visited = [[0] * w for _ in range(h)]
# # for a in arr:
# #     print(a)
# # print()
#
# N = int(input())
# result = 0
# for idx in range(N):
#     d, n = map(int, input().split())
#     if d == 1:
#         arr[0][n] = idx+1
#     elif d == 2:
#         arr[-1][n] = idx+1
#     elif d == 3:
#         arr[n][0] = idx+1
#     elif d == 4:
#         arr[n][-1] = idx+1
# #
# # for a in arr:
# #     print(a)
# # print()
#
# a, b = map(int, input().split())
# if a == 1:
#     x, y = 0, b
# elif a == 2:
#     x, y = h-1, b
# elif a == 3:
#     x, y = b, 0
# elif a == 4:
#     x, y = b, w-1
#
# for n in range(1, N+1):
#     visited = [[0] * w for _ in range(h)]
#     dfs(x, y, n)
#
# print(result)
#
