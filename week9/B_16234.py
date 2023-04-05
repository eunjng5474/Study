dx = [0, 1] # 우 하
dy = [1, 0]
#
# def sol(x, y):
#     for d in range(2):
#         nx = x + dx[d]
#         ny = y + dy[d]
#
#         if 0 <= nx < N and 0 <= ny < N:
#             if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
#                 lst.add((x, y))
#                 lst.add((nx, ny))





N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0

while True:
    lst = []
    # tmp = 0
    # if not tmp:
    #     union = set()
    union = set()
    for x in range(N):
        for y in range(N):
            tmp = 0
            for d in range(2):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 <= nx < N and 0 <= ny < N:
                    if L <= abs(arr[nx][ny] - arr[x][y]) <= R:
                        union.add((x, y, arr[x][y]))
                        union.add((nx, ny, arr[nx][ny]))
                    else:
                        tmp += 1
            if tmp == 2:
                lst.append(union)
                tmp = 0
                union = set()
    if x == N-1 and y == N-1:
        lst.append(union)


    if not lst:
        break
    cnt += 1

    for l in lst:
        print(l)
    print()

    for l in lst:
        sum_n = 0
        for j in l:
            sum_n += j[2]
        num = sum_n // len(l)

        for k in l:
            arr[k[0]][k[1]] = num

    # for a in arr:
    #     print(a)
    # print()

print(cnt)