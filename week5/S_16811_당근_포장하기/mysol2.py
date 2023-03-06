import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ci = sorted(list(map(int, input().split())))
    result = 1000

    for a in range(N-2):
        for b in range(a+1, N-1):
            # for c in range(b+1, N):
                if ci[a] != ci[a+1] and ci[b] != ci[b+1]:
                    A = a + 1
                    B = b - a
                    C = N-1 - b

                    if A*B*C != 0 and A <= N//2 and B <= N//2 and C <= N//2:
                        cnt = max(A, B, C) - min(A, B, C)
                        if cnt < result:
                            result = cnt
    if result == 1000:
        result = -1

    print(f'#{tc} {result}')

















    #

    # for i in range(N-2):
    #     box[0].append(ci[i])
    #     for j in range(i+1, N-1):
    #         box[1].append(ci[j])
    #         for k in range(j+1, N):
    #             box[2].append(ci[k])
    #             if ci[i] == ci[i+1] or ci[j] == ci[j+1] or len(box[0])*len(box[1])*len(box[2]) == 0:
    #                 box = [[] for _ in range(3)]
    #                 continue
    #
    #             if max(len(box[0]), len(box[1]), len(box[2])) - min(len(box[0]), len(box[1]), len(box[2])) < result:
    #                 result = max(len(box[0]), len(box[1]), len(box[2])) - min(len(box[0]), len(box[1]), len(box[2]))
    # print(f'#{tc} {result}')

