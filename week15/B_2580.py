import sys
input = sys.stdin.readline

arr = [list(map(int, input().split())) for _ in range(9)]
zero_lst = []
for i in range(9):
    for j in range(9):
        if not arr[i][j]:
            zero_lst.append((i, j))

def row_chk(row, num):
    for i in range(9):
        if arr[row][i] == num:
            return False
    return True

def col_chk(col, num):
    for i in range(9):
        if arr[i][col] == num:
            return False
    return True

def square_chk(row, col, num):
    r = (row // 3) * 3
    c = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if arr[r+i][c+j] == num:
                return False
    return True

def check(idx):
    if idx == len(zero_lst):
        for i in range(9):
            print(*arr[i])
        exit()

    x, y = zero_lst[idx]
    for n in range(1, 10):
        if row_chk(x, n) and col_chk(y, n) and square_chk(x, y, n):
            arr[x][y] = n
            check(idx+1)
            arr[x][y] = 0

check(0)

















# def row_check(row):
#     check = [False] * 10
#     for i in range(9):
#         if check[arr[row][i]]:
#             return False
#         check[arr[row][i]] = True
#     if False not in check[1:]:
#         return True
#     return False
#
# def col_check(col):
#     check = [False] * 10
#     for i in range(9):
#         if check[arr[i][col]:
#             return False
#         check[arr[i][col]] = True
#     if False not in check[1:]:
#         return True
#     return False
#
# def