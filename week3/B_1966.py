from collections import deque

T = int(input())

for tc in range(T):
    queue = deque()
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # for i in range(len(arr)):
    i = 0
    while arr:
        # if arr[i] == max(arr):
        queue.append(max(arr))
        arr = arr.remove(max(arr))
        
    print(arr)
    print(queue)
