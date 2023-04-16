import sys
sys.stdin = open('sample_input.txt')

def search(arr):  # 가로 탐색
    global result
    for i in range(N):
        for j in range(N - 4):
            tmp = 0
            for k in range(5):
                if arr[i][j + k] == 'o':
                    tmp += 1
            if tmp == 5:
                result = 'YES'
                return


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 'NO'

    search(arr)

    if result == 'NO':                      # 가로 탐색 했는데 없으면 대각선 탐색

        for i in range(N - 4):
            for j in range(N - 4):
                tmp1 = 0
                tmp2 = 0
                for k in range(5):
                    if arr[j + k][i + k] == 'o':
                        tmp1 += 1
                    if arr[j + k][N - 1 - i - k] == 'o':
                        tmp2 += 1
                if tmp1 == 5 or tmp2 == 5:
                    result = 'YES'
                    break

    if result == 'NO':                      # 전치행렬 통해서 세로 탐색
        arr = list(map(list, zip(*arr)))
        search(arr)

    print(f'#{tc} {result}')