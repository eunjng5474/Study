N = int(input())
arr = [[0] * 100 for _ in range(100)]       # 100 * 100 도화지 만들기

for n in range(N):
    a, b = map(int, input().split())
    for i in range(10):
        for j in range(10):
            arr[a+i][b+j] = 1   # 입력값 기준 10 * 10만큼 1로 바꾸기(색종이)

cnt = 0
for a in arr:
    for i in range(100):
        if a[i] == 1:           # 모든 행 돌면서 1이면 cnt += 1
            cnt += 1
print(cnt)