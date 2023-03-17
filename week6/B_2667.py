cnt = 0
def DFS(x, y):
    global cnt
    # 아래 실행에서 cnt를 리스트에 추가해야하므로 정의한 후 global 불러오기
    arr[x][y] = 0               # 상하좌우 이동은 안 해도 방문한 것이므로
    cnt += 1                    # 0으로 바꾼 후 cnt += 1
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == '1':
                DFS(nx, ny)         # 델타 탐색 하면서 재귀함수 호출 => 움직일 수 있는 범위 내 '1'인 수 cnt


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]  # 상하좌우

N = int(input())
arr = [list(input()) for _ in range(N)]
# visited = [[0] * N for _ in range(N)]
result_lst = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            cnt = 0                     # 1이 있는 구역마다 새로 카운트 하기 위해 cnt = 0
            DFS(i, j)                   # 함수 호출
            result_lst.append(cnt)      # 해당 단지에 대해 조사 끝나면 cnt를 결과 리스트에 추가

# print(result_lst)
result = sorted(result_lst)
print(len(result))
for i in result:
    print(i)