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


# ## 2908 상수
# A, B = input().split()
# a = int(A[::-1])
# b = int(B[::-1])
# print(max(a, b))


# ## 2577 숫자의 개수
# num = 1
# for tc in range(3):
#     num *= int(input())
# num_str = str(num)
#
# lst = [0] * 10
# for n in num_str:
#     lst[int(n)] += 1
# for l in lst:
#     print(l)


## 1157 단어 공부
alphabet = {'a': 0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 'j':0, 'k':0, 'l':0,
'm':0, 'n':0, 'o':0, 'p':0, 'q':0, 'r':0, 's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}
word_inp = input()
word = word_inp.lower()
for w in word:
    for a in alphabet:
        if w == a:
            alphabet[a] += 1

result = sorted(alphabet.items(), key=lambda x:x[1], reverse=True)
if result[0][1] == result[1][1]:
    print('?')
else:
    print(str(result[0][0].upper()))