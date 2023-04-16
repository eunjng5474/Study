N = int(input())
arr = [list(input()) + [0] for _ in range(N)] + [[0] * (N+1)]
result = 0

def count(lst):
    cnt = 1
    mx = 0
    for i in range(len(lst) - 1):
        if lst[i] == lst[i+1]:
            cnt += 1
            if cnt > mx:
                mx = cnt
        else:
            cnt = 1
    return mx



def search(arr):
    global result
    for i in range(N-1):
        for j in range(N):
            # if j+1 < N and arr[i][j] != arr[i][j+1]:    # 가로로 옆자리랑 바꾸기
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            cnt1 = count(arr[i])
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

            # if arr[i][j] != arr[i+1][j]:    # 세로 옆자리랑 바꾸기
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            cnt2 = count(arr[i])
            cnt3 = count(arr[i+1])
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]

            if max(cnt1, cnt2, cnt3) > result:
                result = max(cnt1, cnt2, cnt3)

search(arr)
arr_trans = list(map(list, zip(*arr)))
search(arr_trans)

print(result)








# color = ['C', 'P', 'Z', 'Y']
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def search(arr):
#     global result
#     for i in range(N):
#         max_color_cnt = 0
#         max_color = ''
#         for c in color:
#             cnt = arr[i].count(c)
#             if cnt > max_color_cnt:
#                 max_color_cnt = cnt
#                 max_color = c
#         print(max_color, max_color_cnt)
#         if max_color_cnt == N:
#             result = max_color_cnt
#
#         for j in range(N):
#             if arr[i][j] != max_color:
#                 cnt = max_color_cnt
#                 for d in range(4):
#                     # cnt = max_color_cnt
#                     nx = i + dx[d]
#                     ny = j + dy[d]
#                     if 0 <= nx < N and 0 <= ny < N:
#                         if arr[nx][ny] == max_color and cnt < N:
#                             cnt += 1
#                             break
#                 if cnt > result:
#                     result = cnt
#
# search(arr)
# arr_trans = list(map(list, zip(*arr)))
# search(arr_trans)
# print(result)

        # if j < N-1 and arr[i][j] != arr[i][j+1]:    # 가로로 옆자리랑 바꾸기
        #     arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
        #
        #     cnt = 0
        #     for k in range(N):
        #