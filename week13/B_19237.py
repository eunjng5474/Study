# import sys
# sys.stdin = open('input_shark.txt')

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

# 격자 크기 N, 상어 수 M, 이동 수 k
N, M, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
# 상어별 방향 우선순위
directions = [[list(map(int, input().split())) for _ in range(4)] for _ in range(M)]
# 상하좌우 우선순위
smells = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
# smells = [[] for _ in range(N)] f
# 냄새 시간, 상어 번호, 방향
time = 0
sharks = []

### 처음 위치에 냄새 뿌리기
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            s = arr[i][j]
            sharks.append([s, i, j])  # 상어 좌표 저장 [상어 번호, x좌표, y좌표]
            smells[i][j] = [k, s, order[s-1]]


#### 이동 및 냄새 뿌리기
def move(bsharks):
    sharks = []
    for s in bsharks:
        x, y = s[1], s[2]
        shark = s[0]

        # global shark_cnt
        flag = False
        direc = smells[x][y][2]
        for d in directions[shark-1][direc-1]:
            nx = x + dx[d-1]
            ny = y + dy[d-1]

            if 0 <= nx < N and 0 <= ny < N:
                # 냄새 없는 칸
                if not smells[nx][ny][0]:
                    smells[nx][ny] = [k+1, shark, d]
                    # arr[nx][ny] = shark
                    # sharks.append([shark, nx, ny])
                    flag = True
                    break
                ########이거 우선순위가 틀린 듯. 자기 냄새 있는게 우선 되어야 한다,,,,,,,,,,,,,,,,,,,,,,,
                # # 이번 이동에 냄새 뿌린 경우 => 숫자 더 작은 상어만 남아야 함
                # elif smells[nx][ny][0] == k+1:
                #     # smells[nx][ny] = [smells[nx][ny]]
                #     # smells[nx][ny].append([k, shark, d])
                #     if shark < smells[nx][ny][1]:
                #         small_shark = shark
                #         small_d = d
                #         # sharks[smells[nx][ny][1]] = []
                #     else:
                #         small_shark = smells[nx][ny][1]
                #         small_d = smells[nx][ny][2]
                #         # sharks[shark] = []
                #     smells[nx][ny] = [k+1, small_shark, small_d]
                #     # arr[nx][ny] = small_shark
                #     # shark_cnt -= 1
                #     # sharks[small_shark] = [nx, ny]
                #     # sharks.append([small_shark, nx, ny])
                #     flag = True
                #     break

        # 인접 칸 중 냄새 없는 칸이 없는 경우 => 본인 냄새 있는 칸으로
        if not flag:
            for d in directions[shark-1][direc - 1]:
                nx = x + dx[d - 1]
                ny = y + dy[d - 1]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if smells[nx][ny][1] == shark:
                    smells[nx][ny] = [k+1, shark, d]
                    # arr[nx][ny] = shark
                    # sharks.append([shark, nx, ny])
                    break
        # arr[x][y] = 0
    for i in range(N):
        for j in range(N):
            if smells[i][j][0] == k+1:
                sharks.append([smells[i][j][1], i, j])

    return sharks

def minus_smell():
    for i in range(N):
        for j in range(N):
            if smells[i][j][0]:
                smells[i][j][0] -= 1
                if not smells[i][j][0]:
                    smells[i][j] = [0, 0, 0]

while True:
    time += 1
    if time > 1000:
        break

    sharks = move(sharks)
    minus_smell()

    print('----smells----')
    for s in smells:
        print(s)
    print()

    print('---sharks---')
    print(sharks)
    print()
    print('-----------------')

    if len(sharks) <= 1:
        break

if time > 1000:
    print(-1)
else:
    print(time)











    ######## while 돌 때마다 상어 찾지 말고 상어 정보 따로 저장하자
    # for i in range(N):
    #     for j in range(N):
    #         if arr[i][j]:
    #             chk_shark = arr[i][j]
    #             move(i, j, chk_shark)
