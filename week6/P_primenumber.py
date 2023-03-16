from itertools import permutations

def prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if not n % i:
                return False
    return True


def solution(numbers):
    answer = 0
    nums = []
    for i in range(1, len(numbers) + 1):
        nums.append(list(set(map(''.join, permutations(numbers, i)))))
    # permutations(iterable, r) -> 길이가 r인 순열로 반환
    # [['1', '7'], ['71', '17']]
    num = list(set(map(int, set(sum(nums, [])))))
    # [1, 7, 17, 71]

    for n in num:
        if prime(n):
            answer += 1

    return answer


print(solution('011'))




# def solution(numbers):
#     answer = 0
#     number_lst = sorted(list(map(int, numbers)), reverse=True)
#     result = []
#     tmp = ''
#     for i in range(len(number_lst)):
#         tmp += str(number_lst[i])
#
#     n = int(tmp)
#     prime = [True] * (n + 1)
#     prime[0] = False
#     prime[1] = False
#     for i in range(2, n + 1):
#         if prime[i]:
#             for j in range(i * 2, n + 1, i):
#                 prime[j] = False
#
#     num = ''
#     for i in range(len(numbers)):
#         num += str(number_lst[i])
#         for j in range(len(numbers)):
#             if i != j:
#                 num += str(number_lst[j])
#
#
#     return answer
#
# num = ''
# def make(i):
#     global num, number_lst
#     # for i in range(len(number_lst)):
#     num += str(number_lst[i])
#     for j in range(len(number_lst)):
#         if i != j:
#             make(j)
#
#
# print(solution('17'))
#
# # def check(n):
# #     prime = [True] * (n+1)
# #     prime[0] = False
# #     prime[1] = False
# #     for i in range(2, n+1):
# #         if prime[i]:
# #             for j in range(i*2, n+1, i):
# #                 prime[j] = False
# #
# # numbers = '011'
# # number_lst = sorted(list(map(int, numbers)), reverse=True)
# # print(number_lst)