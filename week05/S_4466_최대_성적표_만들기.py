T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    scores = sorted(list(map(int, input().split())), reverse=True)

    result = sum(scores[:K])
    print(f'#{tc} {result}')






###############
    # result = 0
    # cnt = 0
    # tmp = 0
    # for i in scores:
    #     tmp += i
    #     cnt += 1
    #     if cnt == K:
    #         if tmp > result:
    #             result = tmp
    #         tmp -= i
    #         cnt -= 1
    #
    # print(f'#{tc} {result}')

