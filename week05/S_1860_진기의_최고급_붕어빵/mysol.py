import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    people = sorted(list(map(int, input().split())))
    result = 'Possible'

    if people[0] < M:           # 가장 먼저 도착하는 사람이 M초 전에 오면 impossible
        result = 'Impossible'
    else:
        i = 0
        bread = 0
        while i <= people[-1]:      # 가장 늦게 도착하는 사람이 올 때까지 반복
            i += 1
            if not i % M:           # M초마다 bread K개씩 증가
                bread += K
            if i in people:         # 사람이 도착할 때
                if bread:           # 붕어빵이 존재하면 1씩 감소
                    bread -= 1
                else:                       # 도착했는데 붕어빵이 없으면 impossible
                    result = 'Impossible'
                    break

    print(f'#{tc} {result}')

