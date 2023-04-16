N = int(input())
arr = []
for n in range(N):
    a, b, c = map(int, input().split())
    arr.append([[a, 1], [b, 2], [c, 3]])
    # 비용과 색깔 저장(R = 1, G = 2, B = 3)

for i in range(1, N):
    for j in range(3):
        if arr[i-1][(j+1)%3][0] < arr[i-1][(j+2)%3][0]:
            arr[i][j][0] = arr[i-1][(j+1)%3][0] + arr[i][j][0]
            arr[i][j][1] = arr[i-1][(j+1)%3][1]
        else:
            arr[i][j][0] = arr[i-1][(j+2)%3][0] + arr[i][j][0]
            arr[i][j][1] = arr[i-1][(j+2)%3][1]

result = 10000
for n in range(3):
    if arr[N-1][n][1] != n+1:
        if arr[N-1][n][1] < result:
            result = arr[N-1][n][1]

for a in arr:
    print(a)