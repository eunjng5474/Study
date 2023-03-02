L = int(input())
N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
cake = [0 for _ in range(L+1)]

expect = 0
for i in range(N):      # b - a로 최대 기대값 찾기
    a, b = lst[i]
    if (b-a) > expect:
        expect = b-a
        expect_idx = i+1
print(expect_idx)

real = 0
for j in range(N):
    cnt = 0
    for k in range(lst[j][0], lst[j][1]+1):     # 본인이 작성한 범위 내에서
        if cake[k] == 0:                        # 가져간 적 없는 조각이면
            cake[k] = 1                         # 가져갔다는 표시하고 cnt += 1
            cnt += 1
    if cnt > real:                              # 가져간 조각의 최대값 찾기
        real = cnt
        real_idx = j + 1
print(real_idx)


