import sys
from collections import deque

N, M = map(int, input().split())
# parking = [x for x in range(1, N+1)]
# cars = x for 
parking_fee = {}
car_weight = {}
parking = [[] for _ in range(N)]
q = deque()
result = 0

for n in range(N):
    parking_fee[n] = int(input())
for m in range(M):
    car_weight[m] = int(input())

print(parking_fee)
print(car_weight)

for i in range(2*M):
    x = int(input())

    if x > 0:
        if parking.count(0) == 0:           #####이 조건 수정!!!!!
            q.append(x)
        else:
            for p in range(N):
                if p == 0:
                    parking[p].append(x)
                    # p_idx = parking.index(x)
                    result += (parking_fee[p] * car_weight[p])
    else:
        x = abs(x)
        for p in parking:
            if p == x:
                x_idx = p
        # x_idx = parking.index(x)
        parking.remove(x)

        if q:
            parking.insert(parking[p], q.popleft())
            result += (parking_fee[p] * car_weight[p])
    
    print('parking: ', parking)
    print('q: ', q)

        # incar = q.popleft()
        # parking.append(incar)
        # result += (parking_fee[incar] * car_weight[incar])

print(result)

