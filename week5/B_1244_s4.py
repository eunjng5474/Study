
# def change(i):
#     if switch[i] == 0:
#         switch[i] = 1
#     else:
#         switch[i] = 0
#     return

# n_sw = int(input())
# switch = [-1] + list(map(int, input().split()))
# n_st = int(input())
# for n in range(n_st):
#     gender, num = map(int, input().split())
#     # num_idx = num - 1
#     if gender == 1:
#         for i in range(num, n_sw+1, num):
#             change(i)
#             # if switch[i] == 0:
#             #     switch[i] = 1
#             # else:
#             #     switch[i] = 0
#     else:
#         change(num)
#         for k in range(n_sw//2):
#             if num - k < 1 or num + k:
#                 break
#             if switch[num-k] == switch[num+k]:
#                 change(num-k)
#                 change(num+k)
#             else:
#                 break

#         # x, y = (num_idx-1), (num_idx+1)
#         # while True:
#         #     if 0 <= x-1 < n_sw and 0 <= y+1 < n_sw:
#         #         if switch[x-1] == switch[y+1]:
#         #             x, y = x-1, y+1
#         #     else:
#         #         break
#         # for j in range(x, y+1):
#         #     if switch[j] == 0:
#         #         switch[j] = 1
#         #     else:
#         #         switch[j] = 0

# switch = [2, 3, 6, 2, 34, 6, 3, 4, 32, 56, 7, 67 ,32, 4, 3, 6, 4, 45, 7, 4, 56, 3, 4, 7, 6]

# for i in range(len(switch)):
#     print(switch[i], end=' ')
#     if i % 20 == 19:
#         print()





import sys

n_sw = int(input())
switch = list(map(int, sys.stdin.readline().split()))
n_st = int(input())
for n in range(n_st):
    gender, num = map(int, sys.stdin.readline().split())
    num_idx = num - 1
    if gender == 1:
        for i in range(num_idx, n_sw, num):
            if switch[i] == 0:
                switch[i] = 1
            else:
                switch[i] = 0
    else:
        x, y = num_idx, num_idx
        while True: 
            if 0 <= x-1 < n_sw and 0 <= y+1 < n_sw:
                if switch[x-1] == switch[y+1]:
                    x, y = x-1, y+1
                else:
                    break
            else:
                break
        for j in range(x, y+1):
            if switch[j] == 0:
                switch[j] = 1
            else:
                switch[j] = 0

for i in range(n_sw):
    print(switch[i], end=' ')
    if i % 20 == 19:
        print()

'''
4
0 0 0 0
4
1 1
2 1
1 2
2 2
=> 0 1 1 0
my ans: 1 0 0 1
'''