N = int(input())
times = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x:(x[1], x[0]))
result = 0
# print(times)

tmp = [0, 0]
for n in range(N):
    if times[n][0] >= tmp[1]:
        result += 1
        tmp = times[n]
print(result)





# def search(n):
#     global visited, cnt, result
#     tmp = times[n]
#     visited[n] = True
#     if not visited[n+1] and times[n+1][0] >= tmp[1]:
#         cnt += 1
#         visited[n+1] = True
#         search(n+1)
#         visited[n+1] = False
#     if cnt > result:
#         result = cnt
#
# for t in range(N-2):
#     cnt = 0
#     search(t)




# ##################
# N = int(input())
# times = sorted([list(map(int, input().split())) for _ in range(N)])
# result = 0
# print(times)
# #
# # def solution(i):
# #     n = i
# #     global tmp, cnt, result, times
# #     if cnt > result:
# #         result = cnt
# #
# #     if times[n][0] >= tmp[1]:
# #         cnt += 1
# #         tmp = times[n+1]
# #         n += 1
# #         solution(n)
# #     else:
# #         n += 1
#
#
# #
# for i in range(len(times)):
#     tmp = times[i]
#     cnt = 0
#     n = i+1
#     while True:
#         if n == len(times):
#             break
#
#         if times[n][0] >= tmp[1]:
#             cnt += 1
#             tmp = times[n]
#         n += 1
#
#     if cnt > result:
#         result = cnt
#
#
# print(result)

