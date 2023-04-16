import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

# result = []
# plus = 1
# minus = 1
#
# for i in range(N-1):
#     if nums[i+1] >= nums[i]:
#         plus += 1
#     else:
#         result.append(plus)
#         plus = 1
# result.append(plus)             ### nums의 끝까지 돌고 추가안 된 경우 추가!!
#
# for j in range(N-1):
#     if nums[j+1] <= nums[j]:
#         minus += 1
#     else:
#         result.append(minus)
#         minus = 1
# result.append(minus)
#
# print(max(result))
#



######## 교수님 코드 참고하고 내 식대로 수정
result = 0
plus = 1
minus = 1
for i in range(N-1):
    if nums[i+1] >= nums[i]:
        plus += 1
    else:
        if plus > result:
            result = plus
        plus = 1
if plus > result:           ### 반복문 종료 후 비교하는 조건 넣어주니까 맞음
    result = plus           ### 모든 경우에 대해 비교하도록 잘 생각하기!!!

for j in range(N-1):
    if nums[j+1] <= nums[j]:
        minus += 1
    else:
        if minus > result:
            result = minus
        minus = 1
if minus > result:
    result = minus

print(result)




#
# ######## 시간초과
# def plus(n):
#     global result
#     tmp = []
#     for i in range(n, N):
#         if nums[i] >= nums[i-1]:
#             tmp.append(nums[i-1])
#         else:
#             tmp.append(nums[i-1])
#             break
#     if len(tmp) > len(result):
#         result = tmp
#
# def minus(n):
#     global result
#     tmp = []
#     for i in range(n, N):
#         if nums[i] <= nums[i-1]:
#             tmp.append(nums[i-1])
#         else:
#             tmp.append(nums[i-1])
#             break
#     if len(tmp) > len(result):
#         result = tmp
#
# N = int(input())
# nums = list(map(int, input().split()))
# result = [0]
#
# for n in range(1, N):
#     plus(n)
#     minus(n)
#
# print(len(result))

