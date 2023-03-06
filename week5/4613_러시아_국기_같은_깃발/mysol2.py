import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    result = N * M + 1
    #
    # W_cnt = 0
    # for i in range(N-2):
    #     w_tmp_cnt = arr[i].count('W')
    #     W_cnt += M - w_tmp_cnt
    #
    #     B_cnt = 0
    #     for j in range(i+1, N-1):
    #         b_tmp_cnt = arr[j].count('B')
    #         B_cnt += M - b_tmp_cnt
    #
    #         R_cnt = 0
    #         for k in range(j+1, N):
    #             r_tmp_cnt = arr[k].count('R')
    #             R_cnt += M - r_tmp_cnt
    #
    #         cnt = W_cnt + B_cnt + R_cnt
    #         if cnt < result:
    #             result = cnt
    #
    # print(f'#{tc} {result}')


#### sol2


    for a in range(N-2):
        for b in range(a+1, N-1):
            cnt = 0

            for i in range(a+1):
                # for j in range(M):
                #     if arr[i][j] != 'W':
                #         cnt += 1
                w_cnt = arr[i].count('W')
                cnt += (M - w_cnt)

            for i in range(a+1, b+1):
                # for j in range(M):
                #     if arr[i][j] != 'B':
                #         cnt += 1
                b_cnt = arr[i].count('B')
                cnt += (M - b_cnt)

            for i in range(b+1, N):
                # for j in range(M):
                #     if arr[i][j] != 'R':
                #         cnt += 1
                r_cnt = arr[i].count('R')
                cnt += (M - r_cnt)

            if cnt < result:
                result = cnt

    print(f'#{tc} {result}')