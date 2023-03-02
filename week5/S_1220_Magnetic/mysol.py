import sys
sys.stdin = open('input (1).txt')

for tc in range(1, 11):
    num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = 0

    for j in range(100):
        for i in range(100):
            if arr[i][j] == 1:                      # N극일 때
                if i+1 < 100 and arr[i+1][j] == 0:  # 아랫줄이 범위 내고 0이라면
                    arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j] # 아랫줄의 값과 바꾸기(1을 한 칸 내리기)
                if i == 99:             # 만약 i가 99고 해당 자리가 1이면
                    arr[i][j] = 0       # 밖으로 나가게 되므로 해당 자리를 0으로 바꾸기
                else:
                    continue

            if arr[i][j] == 2:                      # S극일 때도 윗줄에 대해 똑같이 적용
                if 0 <= i-1 and arr[i-1][j] == 0:
                    arr[i][j], arr[i-1][j] = arr[i-1][j], arr[i][j]
                if i == 0:
                    arr[i][j] = 0
                else:
                    continue

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1:          # N극에 대해
                if arr[i+1][j] == 2:    # 아랫줄이 S극이면 교착상태이므로 result += 1
                    result += 1
    # N극은 아래로만 내려가고, N+S극 조합일 때 교착상태이므로 하나에 대해서만 조사사
    print(f'#{tc} {result}')