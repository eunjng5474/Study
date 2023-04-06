import sys
sys.stdin = open('input.txt')

def check():
    for i in range(W):
        cnt = 1
        for j in range(1, D):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                break
        if cnt < K:
            return False
    return True


def sol(cnt, idx):
    global result
    if cnt >= D:
        return

    if cnt > result:
        return

    if check():
        if cnt < result:
            result = cnt
        return

    for d in range(idx+1, D):
        arr[d] = [0] * W
        sol(cnt+1, d)

        arr[d] = [1] * W
        sol(cnt+1, d)

        arr[d] = copy_arr[d]




T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    result = 100000
    copy_arr = []
    for a in arr:
        copy_arr.append(list(a))

    sol(0, -1)
    print(f'#{tc} {result}')




#####
# if lst:
#     for l in lst:
#         if l[1]:
#             copy_arr = []
#             for a in arr:
#                 copy_arr.append(list(a))
#
#             copy_arr[d] = [0] * W
#             search(copy_arr, cnt+1)
#             search(arr, cnt+1)
#
#         else:
#             copy_arr = []
#             for a in arr:
#                 copy_arr.append(list(a))
#
#             copy_arr[d] = [1] * W
#             search(copy_arr, cnt+1)
#             search(arr, cnt+1)
# else:
#     return