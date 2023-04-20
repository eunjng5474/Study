from collections import deque

def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))
    answer = ["ICN"]
    visited = [0] * len(tickets)

    q = []
    q.append("ICN")
    while q:
        print(q)
        start = q.pop()
        for i in range(len(tickets)):
            if tickets[i][0] == start and not visited[i]:
                q.append(tickets[i][1])
                answer.append(tickets[i][1])
                visited[i] = 1
    print(visited)
    return answer

# tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
