# ## 11654 아스키코드
# char = input()
# print(ord(char))


# ## 11720 숫자의 합
# N = int(input())
# nums = list(map(int, input()))
# print(sum(nums))


# ## 2920 음계
# music = list(x for x in range(1, 9))
# nums = list(map(int, input().split()))
#
# if nums == music:
#     print('ascending')
# elif nums == music[::-1]:
#     print('descending')
# else:
#     print('mixed')


# ## 2675 문자열 반복
# T = int(input())
# for tc in range(T):
#     n, string = input().split()
#     n = int(n)
#
#     for s in string:
#         print(s*n, end='')
#     print()


# ## 2475 검증수
# nums = list(map(int, input().split()))
# result = 0
# for n in nums:
#     result += n**2
# print(result%10)


#
# ## 1152 단어의 개수
# string = list(input().split())
# print(len(string))


# ## 10809 알파벳 찾기
# S = input()
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# result = [-1] * 26
# for i in range(len(S)):
#     for j in range(len(alphabet)):
#         if S[i] == alphabet[j] and result[j] == -1:
#             result[j] = i
# print(*result)


