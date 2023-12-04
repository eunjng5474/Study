from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
move = {}
# 사다리와 뱀 기록할 딕셔너리
# 칸마다 최대 하나만 가질 수 있기 때문에(사다리, 뱀 중복 불가) 별도 구분 없이 저장
# {32: 62, 42: 68, 12: 98, 95: 13, 97: 25, 93: 37, 79: 27, 75: 19, 49: 47, 67: 17}
for _ in range(n+m):
    a, b = map(int, input().split())
    move[a] = b

result = 100
visited = [0] * 101

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        now = q.popleft()
        if now == 100:
            # 100에 도착하면 횟수 출력(시작 위치에 1을 저장했기 때문에 1 빼고 출력)
            print(visited[now] - 1)
            break

        for n in range(1, 7):
            next = now + n
            if next in move:
                # 다음 위치에 사다리나 뱀이 있다면 이동
                next = move[next]
            if next > 100 or visited[next]:
                # 범위 벗어나거나 갔던 곳이면 continue
                continue

            visited[next] = visited[now] + 1
            # 이전 위치까지의 횟수 + 1을 저장
            q.append(next)

bfs()