N = int(input())
nums = list(map(int, input().split()))
cal = list(map(int, input().split()))
used = [0] * 4
# + - * //
max_sum = -int(1e9)
min_sum = int(1e9)

def sol(n):
    global max_sum, min_sum
    if used == cal:
        if tmp > max_sum:
            max_sum = tmp
        if tmp < min_sum:
            min_sum = tmp
    else:
        for c in range(N-1):




for d in range(N):
# for c in range(4):

