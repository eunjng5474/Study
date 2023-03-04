import sys
sys.stdin = open('input (13).txt')
#
# dx = [0, 0, 1] # 우 좌 하
# dy = [1, -1, 0]
#
# def search(b):
#     cnt = 0
#     x, y = 0, b
#     visited = [[0] * 100 for _ in range(100)]
#     visited[x][y] = 1
#     while x != 99:
#         # if x == 99 and arr[x][y] == 1:
#         #     return cnt
#         visited[x][y] = 1
#
#         # for d in range(3):
#         #     nx = x + dx[d]
#         #     ny = y + dy[d]
#         #
#         #     if 0 <= nx < 100 and 0 <= ny < 100:
#         #         if arr[nx][ny] == 1 and visited[nx][ny] == 0:
#         #             stack.append((nx, ny))
#
#         if 0 <= y < 99 and arr[x][y+1] == 1 and visited[x][y+1] == 0:
#             # while 0 <= y < 99 and arr[x][y+1] == 1:
#             y += 1
#             # visited[x][y+1] = 1
#             # cnt += 1
#         elif 0 <= y < 99 and arr[x][y-1] == 1 and visited[x][y+1] == 0:
#             # while 0 <= y < 99 and arr[x][y-1] == 1:
#             y -= 1
#             # visited[x][y-]
#                 # cnt += 1
#         else:
#             x += 1
#         cnt += 1
#
#
#     return cnt

for t in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    min_cnt = 10000

    for i in range(100):
        if arr[0][i] == 1:
            x, y = 0, i
            cnt = 0

            while x < 99:
                if 0 <= y-1 and arr[x][y-1] == 1:
                    while 0 <= y and arr[x][y-1] == 1:
                        y -= 1
                        cnt += 1
                elif y+1 < 99 and arr[x][y+1] == 1:
                    while y < 99 and arr[x][y+1] == 1:
                        y += 1
                        cnt += 1
                x += 1

            if cnt <= min_cnt:
                min_cnt = cnt
                result = i
    print(f'#{tc} {result}')