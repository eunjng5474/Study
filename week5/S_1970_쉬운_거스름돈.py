T = int(input())
for tc in range(1, T+1):
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    cnt = [0 for _ in range(8)]
    N = int(input())

    for i in range(8):
        cnt[i] += N // money[i]
        N = N % money[i]
        if N == 0:
            break

    print(f'#{tc}')
    print(*cnt)

