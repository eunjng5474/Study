import sys
sys.stdin = open('input (13).txt')

def sum(i):
    global result
    tmp = 0
    for j in range(100):
        tmp += arr[i][j]
    if tmp > result:
        result = tmp


for t in range(1, 11):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0


    for i in range(100):
        sum(i)

    # for i in range(100):
    #     for j in range(100):
    #         if i > j:
    #             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]

    arr = list(map(list, zip(*arr)))

    for i in range(100):
        sum(i)

    tmp = 0
    for j in range(100):
        tmp += arr[j][j]
        if tmp > result:
            result = tmp

    tmp = 0
    for j in range(99, -1, -1):
        tmp += arr[j][j]
        if tmp > result:
            result = tmp

    print(f'#{tc} {result}')
