N = int(input())
lst = list(map(int, input().split()))
bi_tr = [[] for _ in range(N)]
cnt = 0
def binary_tree(lst, cnt):
    m = len(lst)//2
    bi_tr[cnt].append(lst[m])
    if len(lst) == 1:
        return
    binary_tree(lst[:m], cnt+1)
    binary_tree(lst[m+1:], cnt+1)

binary_tree(lst, cnt)

for i in bi_tr:
    print(*i)