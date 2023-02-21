import sys
from collections import deque

N, M = map(int, input().split())
# parking = [x for x in range(1, N+1)]
# cars = x for 
parking = {}
cars = {}
park_lst = [0] * N
q = deque()
result = 0

for n in range(N):
    parking[n+1] = int(input())
for m in range(M):
    cars[m+1] = int(input())

print(parking)
print(cars)

for i in range(2*M):
    x = int(input())

    if x > 0:
        q.append(x)
        if 0 in park_lst:
            pass
        result += (parking[x] * cars[x])
    else:
        x = abs(x)
        x_idx = q.index(x)
        q.pop(x_idx)


