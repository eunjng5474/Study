# N, M = map(int, input().split())
#
# # lst = list(x for x in range(1, N+1))
# result = []
#
# def sol(n):
#     global tmp
#     visited[n] = True
#     tmp.append(n)
#     if len(tmp) == M:
#         result.append(tmp)
#
#     for i in range(n+1, N+1):
#         if not visited[i]:
#             sol(i)
#
#
# for i in range(1, N+1):
#     tmp = []
#     visited = [False] * (N+1)
#     sol(i)
#
# print(result)


N, M = map(int, input().split())
lst = []

def sol(n):
    # lst.append(n)
    if len(lst) == M:
        print(*lst)
        return
    else:
        for i in range(n+1, N+1):
            lst.append(i)
            sol(i)
            lst.pop()

# for n in range(1, N+1):
#     sol(n)

sol(0)