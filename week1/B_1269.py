# ## sol 1 -> 시간초과

# a, b = map(int, input().split())

# a_li = list(map(int, input().split()))
# b_li = list(map(int, input().split()))

# cnt = 0
# for i in a_li:
#     if i not in b_li:
#         cnt += 1

# for j in b_li:
#     if j not in a_li:
#         cnt += 1

# print(cnt)



## sol 2
import sys

a, b = map(int, input().split())

a_set = set(map(int, sys.stdin.readline().split()))
b_set = set(map(int, sys.stdin.readline().split()))

result = len(a_set - b_set) + len(b_set - a_set)
print(result)


# 시간 감소 위해 1620 문제 참고
# list - list 불가능 -> set으로!