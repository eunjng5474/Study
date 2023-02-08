import sys

N, M = map(int, input().split())
num_lst = [map(int, input().split())]
result_lst = []

for i in range(1<<len(num_lst)):
    tmp = []
    for j in range(len(num_lst)):
        if i & (i<<j):
            tmp.append(num_lst[j])
    if sum(tmp) <= M:
        result_lst.append(sum(tmp))
print(max(result_lst))