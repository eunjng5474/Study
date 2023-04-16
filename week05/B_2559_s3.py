import sys

N, K = map(int, input().split())
lst = list(map(int, sys.stdin.readline().split()))

result = []
tmp = sum(lst[:K])      # 처음부터 K개만큼 더한 값
result.append(tmp)
for i in range(1, N-K+1):   # 1번 인덱스부터 K개씩 더해갈 예정
    sum_n = result[-1] - lst[i-1] + lst[i+K-1]
    # result의 가장 최근 값(앞 자리들에 대해 더한 값) 에서 제일 앞 값 빼고 뒤에 값 더하기
    result.append(sum_n)

print(max(result))






#### sol2 - 시간초과
# max_sum = 0
# for i in range(N-K+1):
#     tmp = 0
#     for k in range(K):
#         tmp += lst[i+k]
#     if tmp > max_sum:
#         max_sum = tmp
#
# print(max_sum)
