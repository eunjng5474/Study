# lst = [int(input()) for _ in range(9)]
# result = []
#
# for i in range(8):
#     for j in range(i+1, 9):
#         idx = [x for x in range(9)]
#         idx.remove(i)
#         idx.remove(j)
#         sum_n = 0
#         for k in idx:
#             sum_n += lst[k]
#         if sum_n == 100:
#             for l in idx:
#                 result.append(lst[l])
#             break
#
# result.sort()
# for r in result:
#     print(r)
#

import sys

inp_lst = [int(sys.stdin.readline().rstrip()) for _ in range(9)]
# delete = sum(lst) - 100
lst = sorted(inp_lst)
tmp = 0

for i in range(8):
    for j in range(i+1, 9):
        if sum(lst) - lst[i] - lst[j] == 100:
            a, b = lst[i], lst[j]
            lst.remove(a)
            lst.remove(b)
            tmp = 1
            break
    if tmp == 1:
        break

for r in lst:
    print(r)

