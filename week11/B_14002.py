import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
dp = [1] * N
result = []

for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            if dp[i] <= dp[j]+1:
                dp[i] = dp[j]+1

sol = max(dp)
for n in range(N):
    if dp[n] == sol:        # dp의 최대값이면
        result.append(nums[n])  # result에 해당 인덱스의 nums값 추가
        cnt = sol-1             # dp값 비교하기 위한 변수 cnt
        j = n-1                 # n번째 인덱스부터 역순으로 탐색
        while j >= 0:
            if dp[j] == cnt:                    # dp값이 cnt이고
                if result[-1] > nums[j]:        # result의 가장 최근 값보다 j번째 nums의 값이 작으면
                    result.append(nums[j])      # result에 추가
                    cnt -= 1
            j -= 1
        break
# 10 20 10 30 20 50 이라면
# dp = [1, 2, 1, 3, 2, 4]
# dp[5] == 4이므로 result에 nums[5]인 50 추가
# 인덱스 4부터 역순으로 보면서 dp[j] == 3인 nums[j]를 result[-1]이랑 비교해서 추가,
# 그다음 dp[j] == 2인 nums[j]를 비교해서 추가


result.sort()
print(sol)
print(*result)


