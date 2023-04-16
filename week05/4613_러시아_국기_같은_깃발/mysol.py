import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = N * M

    W_cnt = 0
    for i in range(0, N-2):
        w_tmp_cnt = arr[i].count('W')
        W_cnt += (M - w_tmp_cnt)

        B_cnt = 0
        for j in range(i+1, N-1):
            b_tmp_cnt = arr[j].count('B')
            B_cnt += (M - b_tmp_cnt)

            R_cnt = 0
            for k in range(j+1, N):
                r_tmp_cnt = arr[k].count('R')
                R_cnt += (M - r_tmp_cnt)
                # print(cnt)

            cnt = W_cnt + B_cnt + R_cnt
            if cnt < result:
                result = cnt

    print(f'#{tc} {result}')






##############
# def sol(idx, tmp):
#     global color, result
#     # while idx != N-1:
#     if tmp > result:
#         return
#     if idx == N-1:
#         return
#
#
#     if idx < N-2:
#         if color[-1] == 'R':  # 이전 줄이 빨강이면 그다음도 빨강이어야 함
#             color.append('R')
#             sol(idx, tmp + w_cnt + b_cnt)
#         elif color[-1] == 'B':
#             for j in range(2):


# w_cnt = arr[i].count('W')
# b_cnt = arr[i].count('B')
# r_cnt = arr[i].count('R')


# if color[-1] == 'R':  # 이전 줄이 빨강이면 그다음도 빨강이어야 함
#     cnt += w_cnt + b_cnt  # 흰색, 파란색 수만큼 칠하기
#     color.append('R')
# elif color[-1] == 'B':
#     for j in range(2):


# if arr[i][j] == 'W':
#     w_num += 1
# if arr[i][j] == 'B':
#     b_num += 1
# if arr[i][j] == 'R':
#     r_num += 1

    #
    # for m in range(M):
    #     if arr[0][m] != 'W':  # 제일 윗줄 흰색으로 칠하기
    #         arr[0][m] = 'W'
    #         result += 1
    #     if arr[N - 1][m] != 'R':  # 제일 아랫줄 빨간색으로 칠하기
    #         arr[N - 1][m] = 'R'
    #         result += 1