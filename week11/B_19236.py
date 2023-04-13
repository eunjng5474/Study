dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]




arr = [[] for _ in range(4)]
for a in range(4):
    lst = list(map(int, input().split()))
    for i in range(4):
        arr[a].append((lst[i*2], lst[i*2+1]))

result = 0
