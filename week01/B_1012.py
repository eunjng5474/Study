import sys
sys.setrecursionlimit(10**6)


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x, y):
    arr[x][y] = 0           # 방문했으면 다시 방문하지 않도록 0으로 바꾸기

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < M and 0 <= ny < N:     # 범위 내에서
            if arr[nx][ny] == 1:            # 1이면 갈 수 있으므로 재귀 호출
                DFS(nx, ny)

    
T = int(input())
for tc in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * N for _ in range(M)]
    result = 0

    for k in range(K):
        a, b = map(int, input().split())
        arr[a][b] = 1 



    # for d in range(4):    
    cnt = 0                         # arr에서 1인 곳 찾아서 함수 돌리면 근방에 1인 곳은 다 0으로 바꾸므로
    for x in range(M):
        for y in range(N):
            if arr[x][y] == 1:      # 1인 곳 찾으면 cnt += 1한 후 함수 호출
                cnt += 1            # 1인 곳을 찾는 횟수가 1이 인접해있는 구역 수를 세는 것과 같음
                DFS(x, y)           

    print(cnt)              




            # for d in range(4):    
            #     if arr[x][y] == 1:
            #         arr[x][y] = 0
            #         nx = x + dx[d]
            #         ny = y + dy[d]

            #         if 0 <= nx < M and 0 <= ny < N:
            #             arr[nx][ny] = 0


            # if cnt == 4:
            #     result += 1

    # for i in arr:
    #     print(i)
    # print()

    # for a in arr:
    #     result += arr.count(0)

        


    # for i in arr:
    #     print(i)
    # print()