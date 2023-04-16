
##########
# 질문 게시판 보고 DFS/BFS 사용해야 한다는 걸 알게됨
# 트리로의 접근만 생각했었는데 이름만 보고 단정짓지 말자,,

import sys
sys.setrecursionlimit(10**6)
from collections import deque

def BFS(start):
    q = deque()
    q.append(start)
    visited[start] = True       # 1번 노드는 부모 노드가 없는데 방문 표시는 하려고 True 

    while q:                    # q가 존재하는 동안 반복
        start = q.popleft()     # popleft한 값을 현재 지점으로
        for i in arr[start]:    # start에서 갈 수 있는 노드들에 대해
            if visited[i] == 0: # 간 적 없으면
                q.append(i)     # q에 추가하고
                visited[i] = start      # 부모 노드(start)에서 자식 노드로 이동한 것이므로
                # visited의 자식 노드 인덱스에 start 저장
                # 즉, visited에는 해당 인덱스의 부모 노드의 번호가 저장됨

N = int(input())
arr = [[] for _ in range(N+1)]
visited = [0] * (N+1)


for i in range(N-1):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

BFS(1)
for v in visited[2:]:
    print(v)





########### sol 2
# 예시나 질문 게시판에서 본 반례의 출력은 맞는데 틀렸다고 뜸. 엣지케이스 모르겠다,,
# 맞았어도 시간초과 떴을 듯


# N = int(input())
# tree = [[] for _ in range(N+1)]
# input_arr = []
# parent = [0] * (N+1)
# tree = [[] for _ in range(N+1)]


# for n in range(N-1):
#     u, v = map(int, input().split())
#     input_arr.append((u, v))

# for i in input_arr:             # 루트 1에 대한 자식 노드 우선 탐색
#     if i[0] == 1:               # u == 1이면
#         tree[1].append(i[1])    # tree의 1번 인덱스에 v값 추가
#         parent[i[1]] = 1        # v의 부모 노드가 1임을 표시
#     elif i[1] == 1:             # v == 1일 때도 마찬가지
#         tree[1].append(i[0])
#         parent[i[0]] = 1

# for j in input_arr:             
#     if parent[j[0]] != 0:           
#         tree[j[0]].append(j[1])
#         parent[j[1]] = j[0]
#     elif parent[j[1]] != 0:
#         tree[j[1]].append(j[0])
#         parent[j[0]] = j[1]

# for p in parent[2:]:
#     print(p)

