import sys
input = sys.stdin.readline
nums = []
#
# def postorder(i):
#     if nums[i]:
#         tree.append(i)
#         if nums[i] > nums[i+1]:
#             left[i] = nums[i+1]
#             postorder(i+1)
#         else:
#             right[i] = nums[i+1]
#             postorder(i+1)




while True:
    try:
        nums.append(int(input()))
    except:
        break

tree = []
left = [[] for _ in range(len(nums))]
right = [[] for _ in range(len(nums))]

for n in range(len(nums)-1):
    # postorder(n)
    if nums[n] > nums[n+1]:
        left[n] = nums[n+1]
    else:
        right[n] = nums[n+1]

# print(tree)
print(left)
print(right)