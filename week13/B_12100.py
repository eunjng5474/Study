from copy import deepcopy
import sys
input = sys.stdin.readline

N = int(input())
input_arr = [list(map(int, input().split())) for _ in range(N)]
result = 0

def move(arr, d):
    if d == 0:      # 상
        for j in range(N):  # 열
            end = 0         # 가장 윗줄 == 끝
            for i in range(1, N):   # 1행 ~
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[end][j]:  # 0이면 끝으로 옮기기
                        arr[end][j] = tmp
                    elif arr[end][j] == tmp:  # 같으면 *2
                        arr[end][j] *= 2
                        end += 1
                    else:
                        end += 1                # 다르면 end += 1 해서 값 옮기기
                        arr[end][j] = tmp
                    # arr[i][j] = 0
                    #### arr[i][j]를 end 이용한 위치에 넣고 이후에 0으로 바꾸면 답 안 나옴,,,,

    if d == 1:      # 하
        for j in range(N):
            end = N-1
            for i in range(N-2, -1, -1):  # 밑(end 윗줄)에서부터 위로
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[end][j]:
                        arr[end][j] = tmp
                    elif arr[end][j] == tmp:
                        arr[end][j] *= 2
                        end -= 1
                    else:
                        end -= 1
                        arr[end][j] = tmp

    if d == 2:      # 좌
        for i in range(N):  # 행
            end = 0
            for j in range(1, N):  # 1열 ~
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[i][end]:
                        arr[i][end] = tmp
                    elif arr[i][end] == tmp:
                        arr[i][end] *= 2
                        end += 1
                    else:
                        end += 1
                        arr[i][end] = tmp

    if d == 3:      # 우
        for i in range(N):
            end = N-1
            for j in range(N-2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    if not arr[i][end]:
                        arr[i][end] = tmp
                    elif arr[i][end] == tmp:
                        arr[i][end] *= 2
                        end -= 1
                    else:
                        end -= 1
                        arr[i][end] = tmp
    return arr


def dfs(arr, cnt):
    global result
    if cnt == 5:
        for n in range(N):
            result = max(result, max(arr[n]))
        return

    for d in range(4):
        tmp_arr = move(deepcopy(arr), d)
        dfs(tmp_arr, cnt+1)


dfs(input_arr, 0)
print(result)











#############
#
# dx = [-1, 1, 0, 0]  # 상하좌우
# dy = [0, 0, -1, 1]
#
# def move(arr, d):
#     moved = [[0] * N for _ in range(N)]
#     # 두 번 움직이지 않도록 새로운 배열 생성
#     ## 위로 이동
#     if d == 0:
#         # 첫 줄은 arr의 첫줄 그대로 가져오기
#         moved[0] = list(arr[0])
#         # 자기 위 값과 비교해서 같은 숫자면 위 숫자에 더해짐
#         for x in range(1, N):
#             for y in range(N):
#                 if arr[x][y]:
#                     if arr[x-1][y] == arr[x][y]:
#                         moved[x-1][y] *= 2
#                         arr[x][y] = 0
#                     else:
#                         moved[x][y] = arr[x][y]
#         # 더해지고 난 뒤 모든 값 가장 위로 올리기
#         for p in range(1, N):
#             for q in range(N):
#                 i, j = p, q
#                 if moved[i][j]:
#                     while i >= 0:
#                         if not moved[i-1][j]:
#                             moved[i-1][j] = moved[i][j]
#                             moved[i][j] = 0
#                         else:
#                             break
#                         i -= 1
#
#     # 아래로 이동
#     elif d == 1:
#         moved[N-1] = list(arr[N-1])
#         for x in range(N-2, -1, -1):
#             for y in range(N):
#                 if arr[x][y]:
#                     if arr[x+1][y] == arr[x][y]:
#                         moved[x+1][y] *= 2
#                         arr[x][y] = 0
#                     else:
#                         moved[x][y] = arr[x][y]
#
#         for p in range(N-2, -1, -1):
#             for q in range(N):
#                 i, j = p, q
#                 if moved[i][j]:
#                     while i < N-1:
#                         if not moved[i+1][j]:
#                             moved[i+1][j] = moved[i][j]
#                             moved[i][j] = 0
#                         else:
#                             break
#                         i += 1
#
#     # 왼쪽으로
#     elif d == 2:
#         # 0열 가져오기
#         for n in range(N):
#             moved[n][0] = arr[n][0]
#
#         # 왼쪽/오른쪽 이동은 열에 대해 먼저 탐색하려고 위치 바꿨는데도 틀림,,,,,
#         # 아 두 칸 이상 떨어진 경우 안 합쳐지는 듯,,
#         for y in range(1, N):
#             for x in range(N):
#                 if arr[x][y]:
#                     if arr[x][y-1] == arr[x][y]:
#                         moved[x][y-1] *= 2
#                         arr[x][y] = 0
#                     else:
#                         moved[x][y] = arr[x][y]
#
#         for q in range(1, N):
#             for p in range(N):
#                 i, j = p, q
#                 if moved[i][j]:
#                     while j >= 0:
#                         if not moved[i][j-1]:
#                             moved[i][j-1] = moved[i][j]
#                             moved[i][j] = 0
#                         else:
#                             break
#                         j -= 1
#
#     # 오른쪽으로
#     else:
#         for n in range(N):
#             moved[n][-1] = arr[n][-1]
#
#         for y in range(N-2, -1, -1):
#             for x in range(N):
#                 if arr[x][y]:
#                     if arr[x][y+1] == arr[x][y]:
#                         moved[x][y+1] *= 2
#                         arr[x][y] = 0
#                     else:
#                         moved[x][y] = arr[x][y]
#
#         for q in range(N-2, -1, -1):
#             for p in range(N):
#                 i, j = p, q
#                 if moved[i][j]:
#                     while j < N-1:
#                         if not moved[i][j+1]:
#                             moved[i][j+1] = moved[i][j]
#                             moved[i][j] = 0
#                         else:
#                             break
#                         j += 1
#     return moved
#     # for a in range(len(arr)):
#     #     arr[a] = list(moved[a])
#
# def dfs(arr, cnt):
#     global result
#     if cnt == 5:
#         for i in range(N):
#             result = max(result, max(arr[i]))
#             # for j in range(N):
#             #     if arr[i][j] > result:
#             #         result = arr[i][j]
#         return
#
#     for d in range(4):
#         tmp_arr = move(deepcopy(arr), d)
#         dfs(tmp_arr, cnt+1)
#
#
# dfs(input_arr, 0)
# print(result)
















#
# def sol(cnt, d):
#     global result
#
#     if cnt == 0:
#         for i in range(N):
#             result = max(result, max(arr[i]))
#         return
#
#     # for d in range(4):
#     visited = [[0] * N for _ in range(N)]
#     for x in range(N):
#         for y in range(N):
#             if arr[x][y]:
#                 while True:
#                     nx = x + dx[d]
#                     ny = y + dy[d]
#                     if visited[nx][ny]:
#                         continue
#
#                     if arr[nx][ny]:
#                         arr[nx][ny] += arr[x][y]
#                         arr[x][y] = 0
#                         visited[nx][ny] = 1
#                         break
#                     elif nx == 0 or ny == 0 or nx == N-1 or ny == N-1:
#                         arr[nx][ny] = arr[x][y]
#                         arr[x][y] = 0
#                         visited[nx][ny] = 1
#                         break
#                     else:
#                         x, y = nx, ny
#
#     sol(cnt-1, 0)
#     sol(cnt-1, 1)
#     sol(cnt-1, 2)
#     sol(cnt-1, 3)
#
#
# sol(5, 0)
# sol(5, 1)
# sol(5, 2)
# sol(5, 3)



    # for x in range(N):
    #     for y in range(N):
    #         if arr[x]
    #         for n in range(N):
    #             for d in range(4):
    #                 nx = x + dx[d] * n
    #                 ny = y + dy[d] * n
    #
    #                 if 0 <= nx < N and 0 <= ny < N:
    #                     if arr[nx][ny] and arr[nx][ny] == arr[x][y]:
    #                         tmp = arr[x][y]
    #                         arr[nx][ny] += tmp
    #                         arr[x][y] = 0
    #                         sol(nx, ny, cnt-1)
    #                         arr[x][y] = tmp
    #
    #                     else:
    #                         if nx == x or ny == y:
    #                             tmp = arr[x][y]
    #                             arr[nx][ny] = tmp
    #                             sol(nx, ny)
    #

# for i in range(N):
#     for j in range(N):
#         if arr[i][j]:

# print(result)