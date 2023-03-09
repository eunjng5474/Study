dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(n):
    answer = 0
    # queen = 0
    for i in range(n):
        arr = [[0] * n for _ in range(n)]
        visited = [0] * n
        arr[0][i] = 1   # 첫번째 줄 i위치에 퀸 배치
        visited[i] = 1
        for j in range(i + 1, n):
            for k in range(n):
                if not visited[k]:
                    tmp = 1
                    for d in range(4):
                        nx = j + dx[d]
                        ny = k + dy[d]

                        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                            tmp = 0
                    if tmp:
                        arr[j][k] = 1
                        visited[k] = 1

        queen = 0
        for a in arr:
            queen += a.count(1)
        if queen == n:
            answer += 1


        # for j in range(n):  # 가로 위치 (첫번째 줄에서의 위치 n가지)
        #     arr[i][j] = 1

    return answer


print(solution(4))