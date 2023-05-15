import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
result = int(1e9)
visited = [0] * 100001

def bfs(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        x = q.popleft()
        if x == K:
            return visited[x] - 1

        for i in [x+1, x-1, x*2]:
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[x] + 1
                q.append(i)
        #
        # if x+1 <= 100000 and not visited[x+1]:
        #     visited[x+1] = visited[x] + 1
        #     q.append(x+1)
        # if x - 1 >= 0 and not visited[x-1]:
        #     visited[x-1] = visited[x] + 1
        #     q.append(x-1)
        # if x*2 <= 100000 and not visited[x*2]:
        #     visited[x*2] = visited[x] + 1
        #     q.append(x*2)

print(bfs(N))


#
# def sol(x, time):
#     global result
#     if x == K:
#         result = min(time, result)
#         return
#     if x > K+1:
#         return
#
#     sol(x*2, time+1)
#     sol(x+1, time+1)
#     sol(x-1, time+1)
#
# sol(N, 0)