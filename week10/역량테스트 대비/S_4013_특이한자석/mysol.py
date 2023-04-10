import sys
sys.stdin = open('input.txt')


def right_check(n, d):
    if n >= 3:
        return
    if arr[n][2] != arr[n+1][6]:
        check[n+1] = 1
        # direction[n] = d
        if d == 1:
            direction[n+1] = -1
            right_check(n + 1, -1)

        else:
            direction[n+1] = 1
            right_check(n + 1, 1)


def left_check(n, d):
    if n <= 0:
        return
    if arr[n][6] != arr[n-1][2]:
        check[n-1] = 1
        # direction[n] = d
        if d == 1:
            direction[n-1] = -1
            left_check(n-1, -1)

        else:
            direction[n-1] = 1
            left_check(n - 1, 1)


T = int(input())
for tc in range(1, T+1):
    K = int(input())
    arr = [list(map(int, input().split())) for _ in range(4)]
    turn = [list(map(int, input().split())) for _ in range(K)]

    for t in turn:
        check = [0, 0, 0, 0]
        direction = [0, 0, 0, 0]
        num = t[0] - 1
        direc = t[1]
        check[num] = 1
        direction[num] = direc

        right_check(num, direc)
        left_check(num, direc)

        # print(check)
        # print(direction)

        for n in range(4):
            if check[n]:
                copy_lst = list(arr[n])
                if direction[n] == 1:
                    arr[n] = [copy_lst[-1]] + copy_lst[:7]
                else:
                    arr[n] = copy_lst[1:] + [copy_lst[0]]

    result = 0
    if arr[0][0]:
        result += 1
    if arr[1][0]:
        result += 2
    if arr[2][0]:
        result += 4
    if arr[3][0]:
        result += 8

    print(f'#{tc} {result}')



    #
    # print(turn)
    # for t in turn:
    #     num = t[0] - 1
    #     copy_lst = list(arr[num])
    #     if t[1] == 1:
    #         arr[num] = [copy_lst[-1]] + copy_lst[:7]
    #         if arr[num][2] != arr[num + 1][6]:
    #             tmp_lst = list(arr[num+1])
    #             arr[num+1] = tmp_lst[1:] + [tmp_lst[0]]
    #         if arr[num][6] != arr[num-1][2]:
    #             tmp_lst = list(arr[num-1])
    #             arr[num-1] = tmp_lst[1:] + [tmp_lst[0]]
    #
    #     else:
    #         arr[num] = copy_lst[1:] + [copy_lst[0]]
    #         if arr[num][2] != arr[num + 1][6]:
    #             tmp_lst = list(arr[num+1])
    #             arr[num+1] = [tmp_lst[-1]] + tmp_lst[:7]
    #         if arr[num][6] != arr[num-1][2]:
    #             tmp_lst = list(arr[num-1])
    #             arr[num-1] = [tmp_lst[-1]] + tmp_lst[:7]
    #
    #     for a in arr:
    #         print(a)
    #     print()
    #
