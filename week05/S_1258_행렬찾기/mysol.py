import sys
sys.stdin = open('input (13).txt')


def search(a, b):
    x, y = a, b
    w_cnt = 1
    while True:         # 가로 길이 탐색
        y += 1
        if arr[x][y] == 0 or y < 0 or y >= n:
            # width.append(w_cnt)
            break
        w_cnt += 1

    x, y = a, b
    h_cnt = 1
    while True:  # 세로 길이 탐색
        x += 1
        if arr[x][y] == 0 or x < 0 or x >= n:
            break
        h_cnt += 1

    for i in range(h_cnt):
        for j in range(w_cnt):
            visited[a + i][b + j] = 1
    size_h_w.append([w_cnt*h_cnt, h_cnt, w_cnt])


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    size_h_w = []
    result = []

    for x in range(n):
        for y in range(n):
            if arr[x][y] != 0 and visited[x][y] == 0:
                search(x, y)

    size = sorted(size_h_w, key=lambda x: (x[0], x[1]))
    cnt = len(size)
    for i in size:
        result.append(i[1])
        result.append(i[2])

    print(f'#{tc} {cnt}', *result)

'''
# 1 2 2 1 1 4 
# 2 4 1 2 5 1 2 4 4 3
# 3 6 1 2 2 3 8 1 3 7 5 8 9 5
# 4 10 1 8 2 5 11 1 12 2 5 6 8 4 6 9 4 15 9 10 10 11
# 5 8 1 6 10 2 2 15 6 11 7 14 11 10 17 7 15 17
# 6 10 1 10 16 1 7 4 4 18 11 7 6 16 18 6 12 11 15 12 13 15
# 7 13 1 13 6 3 19 1 3 12 8 6 12 4 4 14 7 11 15 8 14 10 11 15 10 19 13 20
# 8 15 2 1 3 4 1 22 4 13 8 9 25 3 12 8 9 11 10 17 15 12 13 15 11 18 22 10 18 23 17 25
# 9 18 8 2 3 7 4 10 15 3 9 6 14 4 11 8 7 16 6 21 16 9 10 17 21 14 27 11 17 18 18 20 26 15 20 23 23 27
# 10 20 2 1 13 2 5 6 4 13 14 5 6 15 25 4 9 16 12 14 21 8 16 11 22 9 20 10 10 21 8 29 11 25 15 22 30 12 29 28 28 30
'''




    # d = 0
    # w_cnt = 1
    # h_cnt = 1
    # while stack:
    #     x, y = stack.pop()
    #
    #     nx = x + dx[d]
    #     ny = y + dy[d]
    #
    #     if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0 and visited[nx][ny] == 0:
    #         visited[nx][ny] = 1
    #         stack.append((nx, ny))
    #     else:
    #         if d == 0
    #         d = 1
    #
    #
    # h_cnt = 1
    # while True:         # 세로 길이 탐색
    #     x += 1
    #     if arr[x][y] == 0
    #     # nx = x + 1
        # ny = y

        # if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 0 and visited[nx][ny] == 0:
        #     visited[nx][ny] = 1
        #     h_cnt += 1
        #     x, y = nx, ny
        # else:
        #     height.append(h_cnt)
        #     break

