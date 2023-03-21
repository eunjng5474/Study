############ 재귀
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
chicken = []
house = []
lst = []
visited = []
result = 50*50

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append([i, j])

        if arr[i][j] == 2:
            chicken.append([i, j])
            visited.append([False])

def sol(n):
    global result
    if len(lst) == M:
        # print(lst)
        tmp_sum = 0
        for h in house:
            tmp = 50 * 50
            for c in lst:
            # for h in house:
                distance = abs(h[0] - c[0]) + abs(h[1] - c[1])
                if distance < tmp:
                    tmp = distance
            tmp_sum += tmp
        # print(tmp_sum)
        if tmp_sum < result:
            result = tmp_sum
        return

    else:
        for i in range(n, len(chicken)):
            # if not visited[i]:
            lst.append(chicken[i])
            # visited[i] = True
            sol(i+1)
            lst.pop()
            # visited[i] = False

sol(0)
print(result)







# ################## permutations 쓰면 메모리 초과 -> 조합 사용하기
# from itertools import combinations
#
# N, M = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(N)]
# chicken = []
# house = []
# # chic_cnt = 0
# result = 50*50
#
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == 1:
#             house.append([i, j])
#
#         if arr[i][j] == 2:
#             chicken.append([i, j])
#             # chic_cnt += 1
#
# # for h in house:
# #     tmp = 50*50
#     # for m in range(1, M):
# for p in list(map(list, combinations(chicken, M))):     # M개만큼 조합 만들어서
#     tmp_sum = 0
#     for h in house:     # 집별로 가까운 치킨집 찾아서 최단 거리 tmp로
#         tmp = 50 * 50
#         for c in p:
#         # for h in house:
#             distance = abs(h[0] - c[0]) + abs(h[1] - c[1])
#             if distance < tmp:
#                 tmp = distance
#         tmp_sum += tmp
#     if tmp_sum < result:
#         result = tmp_sum
#
# print(result)

