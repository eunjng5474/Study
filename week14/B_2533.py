import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [0] * (N+1)
dp = [[0, 1] for _ in range(N+1)]
# 각 노드에 대해 [얼리어답터가 아닐 때, 맞을 때]

for n in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

def dfs(now):
    visited[now] = 1
    if len(tree[now]) == 1:  # 리프노드인 경우 dp를 [0, 1]로
        dp[now] = [0, 1]

    for next in tree[now]:
        if not visited[next]:
            visited[next] = 1
            dfs(next)
            dp[now][0] += dp[next][1]
            dp[now][1] += min(dp[next])
            # now가 얼리어답터 아니면 next는 얼리어답터여야 함
            # now가 얼리어답터라면 next는 상관 없으므로 next의 dp에 저장된 값 중 최소값 더해주기

dfs(1)
# print(dp)
print(min(dp[1]))


#
# stack = []
# for n in range(N+1):
#     if len(tree[n]) == 1:
#         stack.append(n)

# def dfs(now):
#     visited[now] = 1
#     for i in tree[now]:
#         if not visited[i]:
#             if lent(tree[i]) == 1:
#

#
# def dfs():
#     global result
#     cnt = 0
#     stack = []
#     for n in range(N + 1):
#         if len(tree[n]) == 1:
#             stack.append(n)
#
#     while stack:
#         now = stack.pop()
#         visited[now] = 1
#         for i in tree[now]:
#             if not visited[i]:
#                 visited[i] = 1
#                 stack.append(i)
#                 cnt += 1
#                 for j in tree[i]:
#                     if not visited[j]:
#                         visited[j] = 1
#
#
#         # if check[now]:
#         #     continue
#         # check[now] = 1
#         # for next in tree[now]:
#         #     if not check[next]:
#         #         check[next] = 1
#         #         cnt += 1
#         #         for k in tree[next]:
#         #             if not check[k]:
#         #                 check[k] = 1
#         #                 stack.append(k)
#     return cnt
#
# print(dfs())




#
    # if not check[now]:
    #     check[now] = 1
    #     for next in tree[now]:
    #         if not check[next]:
    #             check[next] = 1
    #             for k in tree[next]:
    #                 if not check[k]:
    #                     dfs(cnt+1, k)

#
# leaf = 0
# for c in range(1, N+1):
#     if len(tree[c]) == 1:
#         leaf = c
# print(leaf)
# dfs(0, leaf)
# # dfs(0, 1)
# print(result)

