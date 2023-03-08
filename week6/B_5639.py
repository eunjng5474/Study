import sys
input = sys.stdin.readline
nums = []
while True:
    try:
        nums.append(int(input()))
    except:
        break

left = [[] for _ in range(len(nums))]
right = [[] for _ in range(len(nums))]

for n in range(len(nums)-1):
    if nums[n] > nums[n+1]:
        left[n] = nums[n+1]
    else:
        right[n] = nums[n+1]