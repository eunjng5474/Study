import sys
sys.stdin = open('input.txt')

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input())
for tc in range(1, T+1):
    # arr = [[0] * 360 for _ in range(360)]
    N, M, K = map(int, input().split())
    if not M%2:
        input_arr = [[0]*((360-M)//2) + list(map(int, input().split())) + [0]*((360-M)//2) for _ in range(N)]
    else:
        input_arr = [[0] * ((360-M)//2+1) + list(map(int, input().split())) + [0] * ((360-M) // 2) for _ in
                     range(N)]

    if not N%2:
        arr = [[0] * 360 for _ in range((360-N)//2)] + input_arr + [[0] * 360 for _ in range((360-N)//2)]
    else:
        arr = [[0] * 360 for _ in range((360-N)//2+1)] + input_arr + [[0] * 360 for _ in range((360 - N) // 2)]

    visited = []
    max_power = 0
    for a in arr:
        if max(a) > max_power:
            max_power = max(a)
        visited.append(list(a * 2))

    while K:
        K -= 1
        for i in range(360):
            for j in range(360):
                if visited[i][j]:
                    visited[i][j] -= 1

        for x in range(360):
            for y in range(360):
                # for k in range(max_power, 0, -1):
                #     if arr[x][y] == k:
                if arr[x][y] and visited[x][y] == arr[x][y] - 1:
                    visited[x][y] = -1

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if not arr[nx][ny] and visited[nx][ny] == 0:
                            arr[nx][ny] = arr[x][y]
                            visited[nx][ny] = arr[nx][ny] * 2
                    # visited[x][y] = -1

    # for a in arr:
    #     print(a)
    # print()
    #
    # for v in visited:
    #     print(v)
    # print()

    result = 0
    for i in range(360):
        for j in range(360):
            if visited[i][j] > 0:
                result += 1

    print(f'#{tc} {result}')







