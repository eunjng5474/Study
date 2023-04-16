from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
prime = [True] * (N+1)
prime[0] = False
prime[1] = False

for i in range(N+1):
    if prime[i]:
        for j in range(i*2, N+1, i):
            prime[j] = False

for i in range(M, N+1):
    if prime[i] == True:
        print(i)

# result = []






#
# # for i in range(M, N+1):
# i = M
# while i <= N:
#     if not nums:
#         break
#     p = nums.popleft()
#     result.append(p)
#     for j in range(1, N//p+1):
#         try:
#             nums.remove(p*j)
#         except:
#             pass
#     i += 1
#
# for i in range(2, M):
#     for j in range(1, N//i+1):
#         try:
#             result.remove(i*j)
#         except:
#             pass
#
# for r in result:
#     print(r)





#
# while True:
#     if not nums:
#         break
#     p = nums.pop(0)
#     result.append(p)
#     for i in range(N//p+1):
#         try:
#             nums.remove(p*i)
#         except:
#             pass
#
# for i in range(2, M):
#     for j in range(N//i+1):
#         try:
#             result.remove(i*j)
#         except:
#             pass
#
# for r in result:
#     print(r)


## 시간초과
# M, N = map(int, input().split())
#
# for i in range(M, N+1):
#     tmp = 0
#     str_i = str(i)
#     if str_i[-1] not in [0, 2, 4, 6, 8]:
#         for j in range(2, i):
#             if not i % j:
#                 tmp += 1
#         if tmp == 0:
#             print(i)