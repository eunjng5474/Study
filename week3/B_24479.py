# def DFS(start):
#     visited[start] = 1
#     stack = [start]
#     pop_lst = []

#     while stack:
#         start = stack.pop()
#         pop_lst.append(start)
        
#         for next in range(1, N+1):
#             if arr[start][next] == 1 and visited[next] == 0:
#                 stack.append(next)
#             if next == N:
#                 return pop_lst 

#     return pop_lst


# N, M, R = map(int, input().split())
# visited = [0] * (N+1)
# arr = [[0] * (N+1) for _ in range(N+1)]
# # cnt = 0

# for n in range(N):
#     u, v = map(int, input().split())
#     arr[u][v] = 1
#     arr[v][u] = 1

# # print(arr)
# print(DFS(R))
    

################
import sys
sys.setrecursionlimit(10**6)

def DFS(start):
    global cnt
    visited[start] = cnt
    ### 단순히 방문 여부가 아닌 방문 순서 기록을 위해 cnt
    for i in arr[start]:
        if visited[i] == 0:
            cnt += 1        ## 방문한 적 없으면 방문하고(cnt += 1) 재귀 호출
            DFS(i) 
    # next = arr[start]
    # if arr[next] and visited[next] == 0:
    #     DFS(next)

N, M, R = map(int, input().split())
visited = [0] * (N+1)
arr = [[] for _ in range(N+1)]
cnt = 1

for m in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)        ## u에서 갈 수 있는 정점 리스트(arr[u]에 v추가)
    arr[v].append(u)        ## 양방향이므로 v에도 u 추가

for i in range(N+1):        ## 오름차순 방문이므로
    arr[i].sort()           ## 각 정점에 대해 갈 수 있는 리스트 정렬


DFS(R)
for j in range(1, N+1):     ## visited 인덱스 0부터 N까지니까 프린트는 1부터
    print(visited[j])