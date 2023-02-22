import sys
from collections import deque

N, M = map(int, input().split())
parking_fee = {}                    # 주차 공간당 요금 딕셔너리 
car_weight = {}                     # 차량 무게 딕셔너리
parking = [[0] for _ in range(N)]   # 주차 공간
q = deque()                         # 대기장소
result = 0

for n in range(N):
    parking_fee[n] = int(input())
for m in range(M):
    car_weight[m] = int(input())

for i in range(2*M):
    x = int(input())

    if x > 0:                       # 들어옴
        cnt = 0
        for p in range(N):
            if parking[p][0] == 0:  # 앞쪽부터 빈자리 있으면(0)
                parking[p][0] += x  # 해당 자리에 x만큼 더해서 주차 표시
                result += (parking_fee[p] * car_weight[x-1])    
                break
            else:
                cnt += 1
        if cnt == N:        # N개의 주차 공간이 모두 0이 아니면 만석이므로
            q.append(x)     # 대기장소에 추가

    else:                   # 나감
        x = abs(x)
        for i in range(N):
            if parking[i][0] == x:      # 주차공간에서 x찾아서
                x_idx = i               # 해당 인덱스 저장
                parking[x_idx][0] = 0   # 나갔으니까 그 자리는 다시 0으로

                if q:                       # 차량 나갔는데 대기 중인 차량이 있으면
                    pop_num = q.popleft()   # popleft
                    parking[x_idx][0] += pop_num    # 주차 시키고 요금 추가
                    result += (parking_fee[x_idx] * car_weight[pop_num-1])

print(result)
