import sys
input = sys.stdin.readline

def search(idx, bottom, num):
    global result
    while idx != N:
        bottom_idx = arr[idx].index(bottom)
        top_idx = opposite[bottom_idx]
        top = arr[idx][top_idx]

        tmp = list(arr[idx])
        tmp[bottom_idx] = 0
        tmp[top_idx] = 0
        num += max(tmp)
        bottom = top
        idx += 1
    if num > result:
        result = num


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
opposite = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}     # 마주보는 인덱스
result = 0

for i in range(6):
    search(0, arr[0][i], 0)
print(result)






# first_six_idx = arr[0].index(6)
# first_tops = [] # 첫번째 주사위에 대해 6과 그 마주보는 값이 아닌 값들에 대해서
# # 윗면이 될 수 있는 후보로 둠
# for n in range(6):
#     if n != opposite[first_six_idx] and n != first_six_idx:
#         first_tops.append(arr[0][n])
#
# # result = 6
# max_sum = 0
# for t in first_tops:        # 첫번째 주사위에서 윗면의 후보가 될 수 있는 숫자 4개에 대해
#     tmp_lst = [t]
#     lst = []
#     # max_sum = 0
#     for i in range(1, N):
#         t_idx = arr[i].index(tmp_lst[-1])
#         opp_t_idx = opposite[t_idx]
#         tmp_lst.append(arr[i][opp_t_idx])
#         max_num = 0
#         for j in range(6):
#             if j != t_idx and j != opp_t_idx:
#                 if arr[i][j] > max_num:
#                     max_num = arr[i][j]
#         lst.append(max_num)
#
#     if sum(lst) > max_sum:
#         max_sum = sum(lst)
# print(max_sum + 6)  # 첫번째 주사위는 옆면 최대값을 항상 6으로 설정했기 때문에
# # 첫번째 주사위 최대값인 6 더하기
