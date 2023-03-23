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


## 2675 문자열 반복
T = int(input())
for tc in range(T):
    n, string = input().split()
    n = int(n)

    for s in string:
        print(s*n, end='')
    print()
