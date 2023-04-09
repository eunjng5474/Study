import sys
sys.stdin = open('input.txt')

def sol(n):
    visited[n] = 1
    for i in relation[n]:
        if not visited[i]:
            visited[i] = 1
            sol(i)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    relation = [[] for _ in range(N+1)]
    visited = [0] * (N+1)
    for m in range(M):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)

    result = 0
    for n in range(1, N+1):
        if not visited[n]:
            result += 1
            sol(n)
    print(f'#{tc} {result}')