import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = N * M


    for i in range(1, N-1):
        for j in range(M):
            if arr[0][j] != 'W':  # 제일 윗줄 흰색으로 칠하기
                arr[0][j] = 'W'
                result += 1
            if arr[N-1][j] != 'R':  # 제일 아랫줄 빨간색으로 칠하기
                arr[N-1][j] = 'R'
                result += 1

            w_num = arr[i].count('W')
            b_num = arr[i].count('B')
            r_num = arr[i].count('R')






# if arr[i][j] == 'W':
#     w_num += 1
# if arr[i][j] == 'B':
#     b_num += 1
# if arr[i][j] == 'R':
#     r_num += 1