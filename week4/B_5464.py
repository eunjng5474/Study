import sys
from collections import deque

N, M = map(int, input().split())
# parking = [x for x in range(1, N+1)]
# cars = x for 
parking = {}
cars = {}
park_lst = deque()
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
        if len(park_lst) == N:
            q.append(x)
        else: 
            ## 리스트에서 빈 자리에 왼쪽부터 넣도록 수정
            park_lst.append(x)
            result += (parking[x] * cars[x])
    else:
        x = abs(x)
        x_idx = park_lst.index(x)
        park_lst.pop(x_idx)
        # incar = q.popleft()
        # park_lst.append(incar)
        # result += (parking[incar] * cars[incar])

print(result)

