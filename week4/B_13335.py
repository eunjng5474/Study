import sys
from collections import deque

n, w, L = map(int, input().split())
weight = deque(map(int, sys.stdin.readline().split()))      # 트럭 무게 리스트 (=> 대기)
bridge = deque()                                            # 다리 위
for i in range(w-1):                                        # w-1만큼 0으로 채우고
    bridge.append(0)
bridge.append(weight[0])                                    # 다리 제일 마지막에 첫번째 트럭 올리기
weight.popleft()                                            # 올렸으니까 popleft, 시간은 1
time = 1            

while True:
    bridge.popleft()                                
    if weight and sum(bridge) + weight[0] <= L:     
        # 대기 중인 트럭이 있고 현재 다리 위 트럭들의 무게 합 + 다음 무게 < L이면
        bridge.append(weight.popleft())     # 대기 첫번째를 다리 위로 올리기
    else:
        bridge.append(0)                    # 최대하중 넘어가면 0을 추가해서 다리 위 트럭이 이동만 하도록
    time += 1                               # 한 번 이동할 때마다(popleft - append) 시간 + 1
    
    if not weight and sum(bridge) == 0:     # 만약 대기 중인 트럭이 없고 다리 위에도 모두 0이면 다 지나간 것
        break

print(time)











###########################
# wait = deque()
# truck_sum = 0
# time = 0

# for i in weight:
#     wait.append((i, w))

# # print(wait)

# while bridge or wait:
#     # if len(bridge) < w and wait:
#     if wait:
#         truck_wgt, bri_time = wait.popleft()
#         if len(bridge) < w and truck_sum + truck_wgt <= L:
#             bridge.append((truck_wgt, bri_time))
#             truck_sum += truck_wgt
#             bri_time -= 1

#     if bri_time == 0:
#         bridge.popleft()
#         truck_sum - truck_wgt
            
#     time += 1

# print(time)



