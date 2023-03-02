N = int(input())
times = sorted(list(map(int, input().split())))
result = 0

# idx_lst = list(enumerate(times))
# lst = sorted(idx_lst, key=lambda x: x[1])
tmp = 0
for i in times:
    tmp += i
    result += tmp
print(result)