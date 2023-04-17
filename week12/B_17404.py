import sys
input = sys.stdin.readline

N = int(input())
arr = []
for n in range(N):
    a, b, c = map(int, input().split())
    arr.append([[a, 1], [b, 2], [c, 3]])
    # 비용과 색깔 저장(R = 1, G = 2, B = 3)

result = int(1e9)

# 첫번째 집에 대해 3가지 경우 모두 해보기
for k in range(3):
    dp = [[[0, 0] for i in range(3)] for _ in range(N)]
    dp[0] = arr[0]
    # 원본 arr가 변하면 안 되므로 dp 별도로 만들어서 첫줄만 복사

    # 두번째 줄에는 첫번째 집에서 칠한 색(k)에 대한 비용 + 본인 비용
    for m in range(3):
        if m == k:
            dp[1][m][0] = int(1e9)
            # k번째 색 칠할 수 없으므로 이후 선택되지 않도록 최대값 넣어두기
        else:
            dp[1][m][0] = dp[0][k][0] + arr[1][m][0]
            dp[1][m][1] = k+1

    # 2부터는 RGB거리 1과 같에 진행하는데,
    # dp[i][j]의 0번째 인덱스에는 누적 비용, 1번째에는 첫번째 집의 색 계속 가져오기
    for i in range(2, N):
        for j in range(3):
            if dp[i-1][(j+1)%3][0] < dp[i-1][(j+2)%3][0]:
                dp[i][j][0] = dp[i-1][(j+1)%3][0] + arr[i][j][0]
                dp[i][j][1] = dp[i-1][(j+1)%3][1]
            else:
                dp[i][j][0] = dp[i-1][(j+2)%3][0] + arr[i][j][0]
                dp[i][j][1] = dp[i-1][(j+2)%3][1]

    for n in range(3):
        # N번 집의 색(n)이 첫번째 집의 색(k+1)과 같으면 result와 비교 x
        if n+1 == dp[N-1][n][1]:
            continue
        if dp[N-1][n][0] < result:
            result = dp[N-1][n][0]

print(result)



'''
[[26, 1], [40, 2], [83, 3]]
[[1000000000, 0], [86, 1], [83, 1]]
[[96, 1], [172, 1], [185, 1]]
## k=0이므로 n=0인 96은 최소값 불가

[[26, 1], [40, 2], [83, 3]]
[[89, 2], [1000000000, 0], [97, 2]]
[[110, 2], [178, 2], [188, 2]]
## 110이 최소값으로 저장

[[26, 1], [40, 2], [83, 3]]
[[132, 3], [143, 3], [1000000000, 0]]
[[156, 3], [221, 3], [231, 3]]
## 110보다 작은 값 없음
'''












#

# result = int(1e9)
# for j in range(3):
#     dp = [[0] * 3 for _ in range(N)]
#     dp[0] = arr[0]
#
#     for i in range(1, N):
#         dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
#         dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
#         dp[i][2] = min(dp[i-1][1], dp[i-1][0]) + arr[i][2]
#
#     for k in range(3):
#         if k == j:
#             continue
#         if dp[N-1][k] < result:
#             result = dp[N-1][k]
#
#
# print(result)