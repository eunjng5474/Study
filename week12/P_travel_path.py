def solution(tickets):
    tickets.sort(key=lambda x: (x[1], x[0]))
    answer = []
    tmp = ["ICN"]
    visited = [0] * len(tickets)

    def dfs(start, tmp):
        if 0 not in visited:
            # 항공권 모두 사용했으면 추가
            answer.append(tmp)
            return

        for i in range(len(tickets)):
            # 현재 위치에서 갈 수 있고 사용한 적 없는 항공권이면
            if tickets[i][0] == start and not visited[i]:
                visited[i] = 1  # 항공권 사용
                dfs(tickets[i][1], tmp+[tickets[i][1]])     # tmp에 다음 경로 추가
                visited[i] = 0

    dfs("ICN", tmp)
    # 정렬했으므로 answer에 가장 먼저 들어간 값이 알파벳 순서 앞서는 경로
    # 그러면 그 이후로 함수 실행할 필요 없는데 append 하고 함수 종료시키면 시간 단축될 거 같은데 라고 생각했었는데
    # return 해줘야 함
    return answer[0]


# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))


# 파이참 안 쓰고 프로그래머스에서만 하는 데 익숙해지자