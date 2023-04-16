import sys
input = sys.stdin.readline

N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)])
result = 0

max_idx = lst[-1][0]
max_height = 0
for i in range(N):
    if lst[i][1] > max_height:
        max_height = lst[i][1]

arr = [[0] * (max_idx+1) for _ in range(max_height+1)]

for l in lst:
    for k in range(l[1]):
        arr[max_height-k][l[0]] = 1

for i in range(max_height+1):
    for j in range(max_idx+1):
        if arr[i][j]:
            cnt = 0
            while j < max_idx:
                j += 1
                if arr[i][j] == 1:
                    result += cnt
                    break
                else:
                    cnt += 1
for i in range(N):
    result += lst[i][1]
print(result)



