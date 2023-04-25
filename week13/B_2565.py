N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [1] * (N+1)

lst.sort(key=lambda x:x[0])
# 첫번째 값을 기준으로 정렬한 뒤
# 두번째 값으로 가긴분수 구하면 됨

for i in range(1, N):
    for j in range(i):
        if lst[i][1] > lst[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))