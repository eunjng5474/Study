import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]    # 상하좌우 좌상 우상 좌하 우하
dy = [0, 0, -1, 1, -1, 1, -1, 1]

arr = [list(map(int, input().split())) for _ in range(19)]
opposite = {0: 1, 1: 0, 2: 3, 3: 2, 4: 7, 5: 6, 6: 5, 7: 4}
result = 0
omok_lst = []

def search(i, j):
    global result, result_x, result_y
    stone = arr[i][j]
    for d in range(8):
        cnt = 1
        stack = []
        x, y = i, j
        while True:
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < 19 and 0 <= ny < 19 and arr[nx][ny] == stone:
                cnt += 1
                stack.append((nx, ny))
                x, y = nx, ny
            else:
                break

        if cnt == 5 and arr[i + dx[opposite[d]]][j + dy[opposite[d]]] != stone:
            result = stone
            stack.append((i, j))
            for a, b in stack:
                omok_lst.append([a+1, b+1])
            # result_x = i + 1
            # result_y = j + 1
            return

check = 0
for i in range(19):
    for j in range(19):
        if arr[i][j]:
            search(i, j)
            if result:
                check = 1
                break
    if check:
        break

result_lst = sorted(omok_lst, key=lambda x: (x[1], x[0]))
print(result)
if result:
    print(*result_lst[0])








# arr = list([[0] * 21] + [[0] + list(map(int, input().split())) + [0] for _ in range(19)] + [[0] * 21])
# result = 0
# result_w, result_h = 0, 0
# check = 0
#
# for i in range(19):
#     for j in range(19):
#         if arr[i][j]:
#             stone = arr[i][j]
#             w_cnt = 0
#             c1_cnt = 0
#             c2_cnt = 0
#             for k in range(6):
#                 if j+k < 19 and arr[i][j+k] == stone:    # 가로
#                     w_cnt += 1
#
#                 if i+k < 19 and j+k < 19 and arr[i+k][j+k] == stone:  # 대각선
#                     c1_cnt += 1
#                 if i+k < 19 and 0 <= j-k and arr[i+k][j-k] == stone:
#                     c2_cnt += 1
#
#             if (w_cnt == 5 and arr[i][j-1] != stone) or (c1_cnt == 5 and arr[i-1][j-1] != stone) or (c2_cnt == 5 and arr[i-1][j+1] != stone):
#                 result = stone
#                 result_w = i
#                 result_h = j
#                 check = 1
#                 break
#
#     if check:
#         break
#
# if not result:
#     arr_trans = list(map(list, zip(*arr)))
#
#     for i in range(19):
#         for j in range(19):
#             if arr_trans[i][j]:
#                 stone = arr_trans[i][j]
#                 h_cnt = 0
#                 for k in range(6):
#                     if j+k < 19 and arr[i][j+k] == stone:    # 세로
#                         h_cnt += 1
#
#                 if h_cnt == 5 and arr[i][j-1] != stone:
#                     result = stone
#                     result_h = i
#                     result_w = j
#                     check = 1
#                     break
#         if check:
#             break
#
# print(result)
# if result:
#     print(result_w, result_h)
