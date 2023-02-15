dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # 상하좌우

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            x, y = i, j            
            break
        break

# print(x, y)
stack = [(x, y)]
visited[x][y] = 1
# print(stack)
cnt = 0
while stack:
    x, y = stack.pop()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < N and 0<= ny < N:              # 범위 벗어나지 않게 조건 달기!!
            if arr[nx][ny] == '1' and visited[nx][ny] == '0':
                stack.append((nx, ny))              # 튜플로 추가
                visited[nx][ny] = 1
                cnt += 1
        print(stack)

print(cnt)        


'''
4
0110
0110
1110
0000
'''