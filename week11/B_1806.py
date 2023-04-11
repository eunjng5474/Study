############ 수정하기


N, S = map(int, input().split())
nums = list(map(int, input().split()))

sum_n = 0
end = 0
result = N

for start in range(N):
    cnt = 1
    while sum_n < S and end < N:
        sum_n += nums[end]
        end += 1
    if sum_n >= S:
        cnt += 1
        result = min(cnt, result)
    sum_n -= nums[start]



print(result)
