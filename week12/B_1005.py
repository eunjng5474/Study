import sys
input = sys.stdin.readline
from collections import deque

def topology():
    q = deque()
    for k in range(1, N+1):
        if not in_degree[k]:
            q.append(k)
            dp[k] = times[k]

    while q:
        now = q.popleft()
        for next in graph[now]:
            in_degree[next] -= 1
            if not in_degree[next]:
                q.append(next)
            dp[next] = max(dp[next], dp[now]+times[next])
                # dp[next] = min(dp[next], dp[now]+times[next])
            ## 이것도 진입차수가 0이 되었을 때 비교해야 하지 않나 싶었는데
            ## 그러면 next의 진입차수가 0이 되지 않았을 때의 now값이랑 비교를 못함
            ## ex) 2, 3 다음 4인데 now == 2일 때 값 갱신 안 됨

T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    dp = [0] * (N+1)
    # dp = [0] + [int(1e9)]*N
    in_degree = [0] * (N+1)

    for k in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_degree[y] += 1

    topology()
    W = int(input())
    print(dp[W])

### 처음에 최소 시간이니까 dp에 최대값 넣어두고 비교할 때 min으로 비교해야하지 않나 생각했었는데
### 먼저 지어져야 하는 건물들이 모두 지어진 다음에 지을 수 있으므로
### max를 해줘야 앞 건물들 모두 다 지어진 다음이 됨