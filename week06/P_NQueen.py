answer = 0


def check(x, y, queen):
    for i in range(x):
        if y == queen[i] or abs(y - queen[i]) == (x - i):
            return False
    return True

    # for i in range(n):    # n까지 줄 i에 대해 모두 확인
    #     # n행의 퀸이 있는 열과 i행의 퀸이 있는 열이 같거나
    #     # 행의 차이만큼 퀸이 있는 열의 차이가 같다면 대각선에 위치하는 것이므로 False
    #     if board[n] == board[i] or abs(board[n] - board[i]) == (n-i):
    #         return False
    # return True


def nqueen(x, n, queen):
    global answer
    if x == n:
        answer += 1
        return

    for y in range(n):
        if check(x, y, queen):
            queen[x] = y
            nqueen(x + 1, n, queen)


#     if n == N:          # 행이 N이 되면 N개의 퀸 모두 놓음
#         answer += 1
#         return

#     for i in range(N):
#         if not visited[i]:
#             board[n] = i    # n행의 i열에 퀸을 놓았다는 표시

#             if check(n):
#                 visited[i] = 1  # 방문 표시 후 다음 행 조사
#                 nqueen(n+1)
#                 visited[i] = 0  # 다시 0으로 설정

def solution(n):
    global answer
    queen = [0] * n
    # visited = [0] * n

    nqueen(0, n, queen)

    return answer





###########
# N = 4
# board = [0] * N
# visited = [0] * N
# result = 0
#
# def check(n):
#     for i in range(n):    # n까지 줄 i에 대해 모두 확인
#         # n행의 퀸이 있는 열과 i행의 퀸이 있는 열이 같거나
#         # 행의 차이만큼 퀸이 있는 열의 차이가 같다면 대각선에 위치하는 것이므로 False
#         if board[n] == board[i] or abs(board[n] - board[i]) == (n-i):
#             return False
#     return True
#
# def nqueen(n):
#     global result
#     if n == N:          # 행이 N이 되면 N개의 퀸 모두 놓음
#         result += 1
#         return
#
#     for i in range(N):
#         if not visited[i]:
#             board[n] = i    # n행의 i열에 퀸을 놓았다는 표시
#
#             if check(n):
#                 visited[i] = 1  # 방문 표시 후 다음 행 조사
#                 nqueen(n+1)
#                 visited[i] = 0  # 다시 0으로 설정
#
# nqueen(0)
# print(result)






# dx = [-1, -1]
# dy = [-1, 1]
#
# def solution(n):
#     answer = 0
#     # queen = 0
#     for i in range(n):
#         arr = [[0] * n for _ in range(n)]
#         visited = [0] * n
#         arr[0][i] = 1   # 첫번째 줄 i위치에 퀸 배치
#         visited[i] = 1
#         for j in range(1, n):
#             for k in range(n):
#                 if not visited[k] and 1 not in arr[j]:
#                     if 0 <= k-1 and k+1 < n:
#                         if arr[j-1][k-1] == 1 or arr[j-1][k+1] == 0:
#                             pass
#                     else:
#                         arr[j][k] = 1
#                         visited[k] = 1
#                     # tmp = 1
#                     # for d in range(2):
#                     #     nx = j + dx[d]
#                     #     ny = k + dy[d]
#                     #
#                     #     if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
#                     #         tmp = 0
#                     # if tmp:
#                     #     arr[j][k] = 1
#                     #     visited[k] = 1
#
#         queen = 0
#         for a in arr:
#             queen += a.count(1)
#         if queen == n:
#             answer += 1
#
#         # for j in range(n):  # 가로 위치 (첫번째 줄에서의 위치 n가지)
#         #     arr[i][j] = 1
#
#     return answer
#
#
# print(solution(8))