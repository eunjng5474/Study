import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ci = sorted(list(map(int, input().split())))
    # result_lst = [[] for _ in range(3)]

    result = 1000
    for i in range(N-2):                 # 소 박스
        for j in range(i+1, N-1):        # 중 박스
            if ci[i] != ci[i+1] and ci[j] != ci[j+1]:   # 같은 크기가 다른 박스에 들어가지 않도록
                A = i + 1               # 소 박스에 들어가는 개수(인덱스 + 1)
                B = j - i
                C = N - 1 - j
                if A * B * C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                    # 빈 박스 없고, 절반 초과하는 박스도 없으면
                    cnt = max(A, B, C) - min(A, B, C)
                    if cnt < result:
                        result = cnt
    if result == 1000:
        result = -1
    print(f'#{tc} {result}')






    # s_cnt = 0
    # for i in range(N-2):
    #     result_lst[0].append(ci[i])
    #     s_cnt += 1
    #
    #     m_cnt = 0
    #     for j in range(i+1, N-1):
    #         result_lst[1].append(ci[j])
    #         m_cnt += 1
    #
    #         l_cnt = 0
    #         for k in range(j+1, N):
    #             result_lst[2].append(ci[k])
    #             l_cnt += 1
    #
    #         for c in range(3):
    #             if len(result_lst[0]) > N//2:
    #                 result = -1
    #                 break
    #
    #         cnt = max(s_cnt, m_cnt, l_cnt) - min(s_cnt, m_cnt, l_cnt)
    #         if cnt < result:
    #             result = cnt
    #
    # print(f'#{tc} {result}')










    # result_lst = []
    #
    # for i in range(N//2):
    #     result_lst[0].append(ci[i])
    # # for j in range(N//2):
    #     result_lst[1].append(ci[N//2+i])
    # # for k in range(N)
    #     try:
    #         result_lst[2].append(ci[2*(N//2)+i])
    #     except:
    #         pass
    # #####
    #
    # result_lst[0].append(ci[0])     # 첫번째 당근을 소 상자에 넣기
    # idx = 0
    # for i in range(1, N):
    #     if result_lst[idx][-1] == ci[i]:
    #         result_lst[idx].append(ci[i])
    #         if len(result_lst[idx]) > N//2:
    #             result = -1
    #             break
    #     else:
    #         for j in range(N
            # if len(result_lst[idx]) < N//2:
            #     result_lst[idx].append(ci[i])
            # else:
            #     idx += 1
            #     result_lst[idx].append(ci[i])
    # if result != -1:
    #     if N % 3 == 0:
    #         result = 0
    #     else:
    #         cnt_lst = [N//3 for _ in range(3)]
    #         j = 0
    #         for i in range(3*(N//3), N):
    #             cnt_lst[j] += 1
    #             j += 1
    #         result = max(cnt_lst) - min(cnt_lst)
    #         # print(cnt_lst)
    #
    # print(f'#{tc} {result}')
    # print(result_lst)
    # print(result)



    # for i in range(N):
    #     result_lst.append(ci[i:i+N//2])
    #     result_lst.append(ci[i+N//2])


