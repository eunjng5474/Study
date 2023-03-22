import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())
m = int(input())

graph = [[]for i in range(n+1)]
visited = [int(1e9)] * (n+1)
for i in range(m):
    start, end, cost = map(int,input().split())
    graph[start].append((cost,end))

s ,e = map(int,input().split())
visited[s] = 0

def dijkstra(start):
    q = []
    heappush(q,start)
    while q:
        cost, now = heappop(q)
        if visited[now] < cost:
            continue
        for i in graph[now]:
            res = cost + i[0]
            if res < visited[i[1]]:
                visited[i[1]] = res
                heappush(q,(res,i[1]))

dijkstra((0,s))
print(visited[e])