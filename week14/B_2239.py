import sys
sys.stdin = open('input_2239.txt')

def check(arr):
    # 가로 확인
    flag = False
    for x in range(9):
        row_cnt = [0] * 10
        for y in range(9):
            if row_cnt[arr[x][y]] >= 1:
                flag = True
                break
            row_cnt[arr[x][y]] += 1
        if 0 in row_cnt[1:]:
            flag = True
            break

    if flag:
        return

    # 세로 확인
    for y in range(9):
        col_cnt = [0] * 10
        for x in range(9):
            if col_cnt[arr[x][y]] >= 1:
                flag = True
                break
            col_cnt[arr[x][y]] += 1
        if 0 in col_cnt[1]:
            flag = True
            break

    if flag:
        return

    # 사각형 확인





input_arr = [list(map(int, input().split())) for _ in range(9)]