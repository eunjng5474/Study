import sys
input = sys.stdin.readline

def plus(i):
    global result
    tmp = []
    # for

    # global result
    # tmp = [nums[i]]
    # for j in range(i+1, N):
    #     if tmp[-1] <= nums[j]:
    #         tmp.append(nums[j])
    # if len(tmp) > len(result):
    #     result = tmp

def minus(i):
    global result
    tmp = [nums[i]]
    for j in range(i+1, N):
        if tmp[-1] >= nums[j]:
            tmp.append(nums[j])
    if len(tmp) > len(result):
        result = tmp

N = int(input())
nums = list(map(int, input().split()))
result = [0]

for i in range(N):
    plus(i)
    minus(i)

print(len(result))