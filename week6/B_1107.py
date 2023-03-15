import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
if M != 0:
    nums = list(map(int, input().split()))


# now = 100
max_cnt = abs(N - 100)
cnt = 0
str_N = str(N)


if N == 100:
    print(0)
elif M == 0:
    print(len(str_N))
else:
    possible = []
    for i in range(0, 10):
        if i not in nums:
            possible.append(i)

    for i in range(len(str_N)):
        if int(str_N[i]) not in nums:
            cnt += 1
        else:
            tmp = 9
            for k in possible:
                if abs(k - int(str_N[i])) < tmp:
                    tmp = abs(k - int(str_N[i]))
            cnt += tmp * 10**(len(str_N) - i - 1) + 1
    if cnt < max_cnt:
        print(cnt)
    else:
        print(max_cnt)



