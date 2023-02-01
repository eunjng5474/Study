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
a, b = map(int, input().split())

a_li = list(map(int, input().split()))
b_li = list(map(int, input().split()))

ab_li = list(a_li - b_li)
ba_li = list(b_li - a_li)

print(len(ab_li) + len(ba_li))