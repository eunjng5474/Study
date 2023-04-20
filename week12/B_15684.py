import sys
input = sys.stdin.readline

def check():
    cnt = 0
    for i in range(1, N+1):
        chk = i
        for j in range(1, H+1):
            if arr[j][chk] == 1:
                chk += 1
            elif arr[j][chk-1] == 1:
                chk -= 1
        if chk == i:
            cnt += 1
    if cnt == N:   # 모든 세로선이 조건 충족해야 True!!!
        return True
    return False


def add_line(idx, add_cnt):  # 가로선 추가
    global result
    if add_cnt >= result:
        return

    if check():
        result = min(result, add_cnt)
        return

    # possible[idx]는 이미 사용했으므로 그 다음 인덱스부터 탐색
    for k in range(idx+1, len(possible)):
        x, y = possible[k]
        arr[x][y] = 1
        add_line(k, add_cnt+1)
        # 지금 인덱스의 다음부터 조사해야하므로 재귀 호출 시 k를 인덱스로 넣기
        arr[x][y] = 0

    ### 함수 호출될 때마다 가로선 놓을 수 있는지 확인하면 시간초과
    # for i in range(1, H+1):
    #     for j in range(1, N):
    #         if not arr[i][j]:
    #             if not arr[i][j-1] and not arr[i][j+1]:
    #                 arr[i][j] = 1
    #                 add_line(add_cnt+1)
    #                 arr[i][j] = 0


N, M, H = map(int, input().split())
arr =[[0] * (N+1) for _ in range(H+1)]
for m in range(M):
    a, b = map(int, input().split())
    arr[a][b] = 1
    # arr[a][b+1] = 1   # 이거 추가하면 연결 안 하는 두 세로선도 이어지게 됨
    # 그냥 1이면 오른쪽 이동
    # -1의 인덱스가 1이면 왼쪽으로 이동


# 시간초과 안 뜨려면 처음 한 번 가능한지 확인해서 리스트에 추가해놓기
possible = []
for i in range(1, H+1):
    for j in range(1, N):
        if not arr[i][j]:       # 나, 양옆 모두 0이어야 내 자리에 놓을 수 있음
            if not arr[i][j-1] and not arr[i][j+1]:
                possible.append((i, j))


result = 4
add_line(-1, 0)     # possible의 0번째 인덱스부터 다 체크해야하므로 (-1, 0)
if result > 3:
    result = -1

print(result)
# 만두 코드 참고,,,,,,,,,,,,,






# # 시작 세로선의 인덱스, x, y좌표, 추가 선 개수
# def sol(s_idx, x, y, add_cnt):
#     global result, check_cnt
#     if x == N+1:
#         if y == s_idx:
#             check_cnt += 1
#         else:
#             return
#
#     if add_cnt > result:
#         return
#
#     # if check_cnt == N:
#     #     result = min(result, add_cnt)
#     #     return
#
#     if arr[x][y] == 1:
#         if arr[x][y+1] == 1:
#             sol(s_idx, x, y+1, add_cnt)
#         if arr[x][y-1] == 1:
#             sol(s_idx, x, y-1, add_cnt)
#
#     if x > 0 and not arr[x][y]:
#         arr[x][y] = 1
#         arr[x][y+1] = 1
#         sol(s_idx, x, y, add_cnt+1)
#         arr[x][y] = 0
#         arr[x][y+1] = 0
#
#     sol(s_idx, x+1, y, add_cnt)


# check_cnt = 0
# for n in range(N):
#     sol(n, 0, n, 0)
#
# if result > 3:
#     result = -1
# if check_cnt == 0:
#     result = -1
# print(result)
#