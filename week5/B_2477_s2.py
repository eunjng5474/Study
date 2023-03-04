# 교수님 코드 참고
import sys
input = sys.stdin.readline

K = int(input())
lst = [list(map(int, input().split())) for _ in range(6)]

big_w = 0
big_h = 0
small_w = 0
small_h = 0

for i in range(6):
    d, n = lst[i]
    if i % 2:               # 가로 다음 세로, 세로 다음 가로
        if n > big_w:
            big_w = n
    else:
        if n > big_h:
            big_h = n

for i in range(6):
    if i % 2:
        if lst[(i-1) % 6][1] + lst[(i+1) % 6][1] == big_h:          ## (i+-1) % 6 !!!
            small_w = lst[i][1]
    else:
        if lst[(i-1) % 6][1] + lst[(i+1) % 6][1] == big_w:
            small_h = lst[i][1]

result = (big_h * big_w) - (small_h * small_w)
print(result * K)







######## 런타임 에러
# width = {}
# height = {}
# K = int(input())
# for t in range(1, 7):                   # 딕셔너리[인덱스] = 입력값
#     d, n = map(int, input().split())
#     if d in [1, 2]:
#         width[t] = n        # 가로
#     else:
#         height[t] = n       # 세로
#
# max_w = 0
# max_h = 0
# for idx, item in width.items():     # 최대 높이
#     if item > max_w:
#         max_w = item
#         max_w_idx = idx
#
# for idx, item in height.items():    # 최대 너비
#     if item > max_h:
#         max_h = item
#         max_h_idx = idx
#
#
# # 전후 인덱스에 해당하는 값들의 합이 최대 높이/너비라면
# # 해당 인덱스에 해당하는 값은 전체 사각형에서 빼줄 작은 사각형의 높이/너비
# small_w = 0
# small_h = 0
# for idx in range(2, 6):
#     if height[idx-1] + height[idx+1] == max_h:
#         # if height[idx-1] + height[idx+1] == max_h:  1 < idx < 6 and
#         small_w = item
#
# for idx in range(2, 6):
#     if width[idx-1] + width[idx+1] == max_w:
#         # if width[idx-1] + width[idx+1] == max_w:
#         small_h = item
#
# # 전체 큰 사각형의 넓이 - 작은(빈) 사각형의 넓이
# result = (max_h * max_w) - (small_h * small_w)
# print(result * K)


###############3
#
# row = []
# col = []
# K = int(input())
# for t in range(1, 7):
#     d, n = map(int, input().split())
#     if d in [1, 2]:
#         row.append((t, n))
#     else:
#         col.append((t, n))
#
# max_row_idx = 0
# max_row = 0
# for i in row:
#     if i[1] > max_row:
#         max_row = i[1]
#         max_row_idx = i[0]
#
# short_col = 500
# short_col_idx = 0
# for j in col:
#     if j[0] == max_row_idx - 1:
#         if j[1] < short_col:
#             short_col = j[1]
#             short_col_idx = j[0]
#     if j[0] == max_row_idx + 1:
#         if j[1] < short_col:
#             short_col = j[1]
#             short_col_idx = j[0]
#
#
# print(row)
# print(col)
# print()
# print(max_row)
# print(short_col)
#
# row = {}
# col = {}
# K = int(input())
# for t in range(1, 7):                   # 딕셔너리[인덱스] = 입력값
#     d, n = map(int, input().split())
#     if d in [1, 2]:
#         row[t] = n
#     else:
#         col[t] = n
# print(row)
# print(col)
# result = 0
# # max_row_idx = 0
# max_row = 0
# for idx, item in row.items():       # 가로 최대길이
#     if item > max_row:
#         max_row = item
#         max_row_idx = idx
#
# max_col = 0
# for idx, item in col.items():       # 세로 최대높이
#     if item > max_col:
#         max_col = item
#         max_col_idx = idx
#
# # 최대높이 전후로 조사해서 (최대길이가 아닌 값 * 최대높이) 우선 계산
# if max_col_idx > 1 and row[max_col_idx-1] != max_row:
#     a = row[max_col_idx-1]
#     result += a * max_col
# elif row[max_col_idx + 1] != max_row:
#     a = row[max_col_idx + 1]
#     result += a * max_col
#
#
#
# if max_row_idx > 1 and col[max_row_idx-1] != max_col:
#     b = col[max_row_idx-1]
# elif col[max_row_idx+1] != max_row:
#     b = col[max_row_idx+1]
#
# for idx, item in row.items():
#     if item != max_row and item != a:
#         c = item
#
# result += b * c
# print(result)




#
# # short_col_idx = 0
# if col[max_row_idx-1] < col[max_row_idx+1]:
#     short_col = col[max_row_idx-1]
#     short_col_idx = max_row_idx-1
# else:
#     short_col = col[max_row_idx+1]
#     short_col_idx = max_row_idx+1
#
# if row[max_row_idx+4]:
#     a = row[max_row_idx+4]
#     b =
# elif row[max_row_idx-4]:
#     a = row[max_row_idx + 4]



