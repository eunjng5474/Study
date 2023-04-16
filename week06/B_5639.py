import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
nums = []

def postorder(s, e):
    if s > e:
        return
    mid = e + 1

    for i in range(s+1, e+1):
        if nums[i] > nums[s]:
            mid = i
            break

    postorder(s+1, mid-1)       # 왼쪽
    postorder(mid, e)           # 오른쪽
    print(nums[s])


while True:
    try:
        nums.append(int(input()))
    except:
        break

postorder(0, len(nums)-1)



# tree = [[] for _ in range(len(nums))]
# left = [[] for _ in range(len(nums))]
# right = [[] for _ in range(len(nums))]
#
# for n in range(len(nums)-1):
#     # postorder(n)
#     if nums[n] > nums[n+1]:
#         left[n] = nums[n+1]
#     else:
#         right[n] = nums[n+1]
#     tree[n] = nums[n]
#
# print(tree)
# print(left)
# print(right)


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
