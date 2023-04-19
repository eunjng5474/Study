import sys
input = sys.stdin.readline

# 시작 세로선의 인덱스, x, y좌표, 추가 선 개수
def sol(s_idx, x, y, add_cnt):
    global result, check_cnt
    if x == N+1:
        if y == s_idx:
            check_cnt += 1
        else:
            return

    if add_cnt > result:
        return

    # if check_cnt == N:
    #     result = min(result, add_cnt)
    #     return

    if arr[x][y] == 1:
        if arr[x][y+1] == 1:
            sol(s_idx, x, y+1, add_cnt)
        if arr[x][y-1] == 1:
            sol(s_idx, x, y-1, add_cnt)

    if x > 0 and not arr[x][y]:
        arr[x][y] = 1
        arr[x][y+1] = 1
        sol(s_idx, x, y, add_cnt+1)
        arr[x][y] = 0
        arr[x][y+1] = 0

    sol(s_idx, x+1, y, add_cnt)






N, M, H = map(int, input().split())
arr = [[0] * (N+2) for _ in range(M+2)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[a][b+1] = 1

result = 4
check_cnt = 0
for n in range(N):
    sol(n, 0, n, 0)

if result > 3:
    result = -1
if check_cnt == 0:
    result = -1
print(result)



for a in arr:
    print(a)