A, B, V = map(int, input().split())

now = 0
cnt = 0
while True:
    now += A
    now -= B
    if now >= V:
        break
    cnt += 1
print(cnt)
