T = int(input())
for tc in range(1, T+1):
    N = int(input())
    aj = list(map(int, input().split()))

    result = -1
    for i in range(N-1):
        for j in range(i+1, N):
            num = aj[i] * aj[j]
            str_num = str(num)
            tmp = []
            for j in range(len(str_num)-1):
                if int(str_num[j]) <= int(str_num[j+1]):
                    tmp.append(j)
                else:
                    break
            if len(tmp) == len(str_num) - 1:
                if num > result:
                    result = num

    print(f'#{tc} {result}')


