import sys
import heapq

hq = []
N = int(input())
for n in range(N):
    x = int(sys.stdin.readline())

    if x != 0:
        heapq.heappush(hq, (abs(x), x))
    else:
        if hq:
            a, b = heapq.heappop(hq)
            print(b)
        else:
            print(0)

# 구글링 참고 - 튜플로 값 추가하면 앞의 값을 기준으로 정렬!





# ###### sol 2 - 시간 초과
# hq = []
# input_num = []
# N = int(input())
# for n in range(N):
#     x = int(sys.stdin.readline())

#     if x != 0:
#         heapq.heappush(hq, abs(x))
#         input_num.append(x)
#     else:
#         if hq:
#             y = heapq.heappop(hq)
#             input_sort = sorted(input_num)
#             for a in input_sort:
#                 if abs(a) == y:
#                     print(a)
#                     input_num.remove(a)
#         else:
#             print(0)
