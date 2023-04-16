## 백트래킹
answer = -1

def dfs(k, cnt, dungeons, visited):
    global answer
    if cnt > answer:
        answer = cnt

    for i in range(len(dungeons)):
        if not visited[i] and k >= dungeons[i][0]:
            visited[i] = True
            dfs(k - dungeons[i][1], cnt+1, dungeons, visited)
            visited[i] = False


def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    dfs(k, 0, dungeons, visited)
    return answer


dungeons = [[80,20],[50,40],[30,10]]
print(solution(80, dungeons))


#### 순열
from itertools import permutations

def solution(k, dungeons):
    answer = -1

    for i in permutations(dungeons, len(dungeons)):
        # print(i)
        tmp = k
        cnt = 0

        for need, spend in i:
            if tmp >= need:
                tmp -= spend
                cnt += 1
        if cnt > answer:
            answer = cnt
    return answer

print(solution(80, dungeons))