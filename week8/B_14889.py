### 가지치기 없이도 시간초과 안 뜨고 패스네,,,,(3084ms)
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
people = [i for i in range(N)]
visited = [0] * N
start_lst = []
# link_lst = []
result = 100 * N * N


def start_sum(lst):     # start팀 점수 계산
    start = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            start += arr[lst[i]][lst[j]]
            start += arr[lst[j]][lst[i]]
    return start

def link_sum(lst):      # link 팀
    link = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            link += arr[lst[i]][lst[j]]
            link += arr[lst[j]][lst[i]]
    return link


def sol(n):
    global result
    if len(start_lst) == N//2:      # 절반이 start_lst에 추가되었으면
        link_lst = []
        start = start_sum(start_lst) # start팀의 sum 구하는 함수 호출

        for p in people:
            if p not in start_lst:  # start 아닌 사람들 link팀으로
                link_lst.append(p)
        link = link_sum(link_lst)   # link팀 점수 구하기

        if abs(start - link) < result:
            result = abs(start - link)

        return

    for i in range(n, N):
        start_lst.append(i)
        sol(i+1)
        start_lst.pop()

sol(0)
print(result)