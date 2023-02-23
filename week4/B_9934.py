import sys

def inorder(i):
    global arr
    global cnt
    if i:
        inorder(left[i])            # 만든 이진트리 순회하면서 arr값 순서대로 입력
        result[i] = arr[cnt]
        cnt += 1
        inorder(right[i])


K = int(input())
arr = list(map(int, sys.stdin.readline().split()))

parent = [0] * (2**K)
left = [0] * (2**K)
right = [0] * (2**K)
result = [0] * (2**K)

i = 1                   # 인덱스로 된 이진 트리 만들기
while True:
    left[i] = i*2
    parent[i*2] = i
    if i*2 == (2**K-1):
        break
    right[i] = i*2+1
    parent[i*2+1] = i
    if i*2+1 == (2**K-1):
        break
    i += 1

cnt = 0
inorder(1)
idx = 1
for i in range(K):
    for j in range(2**i):
        print(result[idx], end=' ')
        idx += 1
    print()
