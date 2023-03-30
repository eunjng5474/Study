import sys
input = sys.stdin.readline

def sol(n):
    global result
    if len(lst) == 5:   # lst에 5명이 들어가면 성공
        result = 1
        return

    for i in people[n]:     # n과 친구인 리스트들 중에서
        if i not in lst:    # lst에 추가된 적 없는 친구 i라면
            lst.append(i)   # 리스트에 추가하고 i에 대해 다시 탐색
            sol(i)
            lst.pop()


N, M = map(int, input().split())
people = [[] for _ in range(N)]

for m in range(M):
    a, b = map(int, input().split())    # 양방향으로 친구임을 저장
    people[a].append(b)
    people[b].append(a)

result = 0
for i in range(N):      # 처음에 이 for문 없이 했더니 틀림
                        # 0부터 시작이 아닌 1~5와 같은 경우 제외되었기 때문인 듯
    if not result:      # 따라서 result == 0일 때
        lst = [i]       # lst에 초기값 i 넣어주고(함수에서는 i의 친구들부터 탐색하므로 리스트에 추가 안 됨) 함수 호출
        sol(i)
print(result)

