
N = int(input())
tree = [[] for _ in range(N+1)]
arr = []

for n in range(N-1):
    u, v = map(int, input().split())
    arr.append((u, v))

# for i in range(N):
#     if 1 in arr[i]:


