import sys
# sys.stdin = open('input_2239.txt')
input = sys.stdin.readline

def row_check(row, num):   # 가로 확인
    for col in range(9):
        if arr[row][col] == num:
            # 넣을 값(num)이 이미 그 줄에 있으면 False
            return False
    return True

def col_check(col, num):    # 세로 확인
    for row in range(9):
        if arr[row][col] == num:
            return False
    return True

def square_check(row, col, num):    # 사각형 확인
    r = row // 3 * 3    # 각 사각형의 첫번째 행/렬로 설정(0, 3, 6 중 1)
    c = col // 3 * 3

    for a in range(3):
        for b in range(3):
            if arr[r+a][c+b] == num:
                return False
    return True

<<<<<<< HEAD
    # 사각형 확인

=======

def dfs(idx):
    if idx == len(zero_idx):  # 0인 값 다 채웠으면 프린트하고 함수 종료
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end="")
            print()
        exit()

    x, y = zero_idx[idx]    # 함수 호출될 때마다 해당 인덱스의 제로 인덱스 값 가져와야 함
    for n in range(1, 10):
        if row_check(x, n) and col_check(y, n) and square_check(x, y, n):  # check 다 통과하면
            arr[x][y] = n
            dfs(idx+1)
            arr[x][y] = 0
>>>>>>> 3b5106d046e80dc45f678f746897e7bb9b8cb495





arr = [list(map(int, input().rstrip())) for _ in range(9)]
zero_idx = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            zero_idx.append((i, j))

dfs(0)






#################


# def row_check(row):     # 가로 확인
#     flag = True
#     row_cnt = [0] * 10
#     for col in range(9):
#         if row_cnt[arr[row][col]] >= 1:
#             flag = False
#             break
#         row_cnt[arr[row][col]] += 1
#     if 0 in row_cnt[1:]:
#         flag = False
#
#     return flag
#
#
# def col_check(col):     # 세로 확인
#     flag = True
#     col_cnt = [0] * 10
#     for row in range(9):
#         if col_cnt[arr[row][col]] >= 1:
#             flag = False
#             break
#         col_cnt[arr[row][col]] += 1
#     if 0 in col_cnt[1]:
#         flag = False
#
#     return flag
#
#
# def square_check():
#     # 사각형 확인
#     for x in range(0, 7, 3):
#         for y in range(0, 7, 3):
#             square_cnt = [0] * 10
#             for i in range(3):
#                 for j in range(3):
#                     if square_cnt[arr[x+i][y+j]] >= 1:
#                         flag = False
#                         break
#                     square_cnt[arr[x+i][y+j]] += 1
#             if 0 in square_cnt[1:]:
#                 flag = False
#                 break
#
#     return flag
#
#
#
# def dfs(cnt):
#     if cnt == zero_cnt:
#         flag = square_check()
#         if not flag:
#             return
#
#         for k in arr:
#             print(*k)
#         exit()
#
#     for x in range(9):
#         for y in range(9):
#             for n in range(1, 10):
#                 if arr[x][y]:
#                     continue
#                 arr[x][y] = n
#                 if row_check(x) and col_check(y):
#                     dfs(cnt+1)
#
#
#
# # input_arr = [list(map(int, input().split())) for _ in range(9)]
# zero_cnt = 0
# arr = []
# for n in range(9):
#     lst = list(map(int, input()))
#     arr.append(lst)
#     zero_cnt += lst.count(0)
#
# dfs(0)