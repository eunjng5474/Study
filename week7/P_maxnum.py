ns = [0, 0, 0, 0]
numbers = list(map(str, ns))

nums = sorted(numbers, key=lambda x:x*3, reverse=True)
# x*3을 기준으로 내림차순으로 정렬
# x는 현재 문자열이고, 원소가 1000 이하이므로 3->333을 기준으로 정렬하기 위해

string = ''
for n in nums:
   string += n

## 처음에 answer += n으로 했었는데 질문게시판 보고
## [0, 0, 0, 0]의 경우 답이 0이 아닌 0000으로 출력되기 때문에
## int로 바꾼 뒤 다시 str으로 변환
answer = str(int(string))
print(string)
print(answer)
















# ############# 시간초과
# from itertools import permutations
#
# def solution(numbers):
#     result_lst = []
#
#     nums = list(map(str, numbers))
#     for i in permutations(nums, len(nums)):
#         string = ''
#         for j in i:
#             string += j
#         result_lst.append(string)
#
#     result = list(map(int, result_lst))
#     answer = str(max(result))
#
#     return answer







#
# def sol(numbers):
#     global cnt, result, tmp
#     if cnt == len(numbers):
#         if int(answer) > result:
#             result = int(answer)
#         return
#     else:
#         for i in range(len(numbers)):
#             tmp += str(numbers[i])
#             cnt += 1
#             sol(i+1)
#             tmp -= str(numbers[i])
#
#
# answer = ''
# cnt = 0
# result = 0
# tmp = ''
#
#
# def solution(numbers):
#     sol(numbers)
#     answer = str(result)
#     return answer
#
# numbers = [6, 10, 2]
# print(solution(numbers))