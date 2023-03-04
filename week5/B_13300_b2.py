import sys

N, K = map(int, input().split())
student = [[0, 0] for _ in range(6)]
##1-0 / 1-1 // 2-0 / 2-1 // ... // 6-0 / 6-1
result = 0

for n in range(N):
    s, y = map(int, sys.stdin.readline().split())
    student[y-1][s] += 1

for i in student:
    for j in i:
        result += j // K
        if j % K:
            result += 1
        # if j % K == 0:
        #     result += (j // K)
        # else:
        #     result += ((j // K) + 1)

print(result)
