N = int(input())
lst = sorted([list(map(int, input().split())) for _ in range(N)])
result = 0
#







######## 둘레 구하고 있었다,,, 면적 구하는 문제임!!!!!!!
# print(lst)
# result += lst[0][1]     # 가장 왼쪽 값의 높이 더하기
# result += lst[-1][1]    # 가장 오른쪽 높이 더하기
#
# max_h = 0
# for i in range(N):
#     if lst[i][1] > max_h:
#         max_h = lst[i][1]
#         max_h_idx = i
#
#
#
# tmp = [lst[0]]      # 가장 최근 값 중 최대높이
# for i in range(1, max_h_idx+1):           # 최대값까지 올라가는 경우
#     if lst[i][1] > tmp[-1][1]:
#         result += (lst[i][0] - tmp[-1][0])     # 현재 - 직전 가로 길이 더하기(그림에서 2~4에 해당하는 2)
#         result += (lst[i][1] - tmp[-1][1])     # 높아진 만큼 길이 더하기(그림에서 6-4에 해당하는 2)
#         tmp.append(lst[i])
#
# result += 1     # 최대높이의 가로길이 더하기
# #
# # tmp = [lst[max_h_idx+1]]
# # for j in range(max_h_idx+1, N):
# #     if
#
#
# #     # if i == max_h_idx:
# #     #     result += 1
# #     #     break
# #
# # result += 1     # 최대값의 가로만큼 더해주기
# tmp_max = 0
# tmp_max_idx = 0
# for j in range(max_h_idx+1, N):
#     if lst[j][1] > tmp_max:
#         tmp_max = lst[j][1]
#         tmp_max_idx = j
# print(result)
# if tmp_max_idx == N-1:      # 최대값 이후 기둥 중에서 최대값이 가장 마지막 기둥이라면
#     result += (lst[tmp_max_idx][0] - lst[max_h_idx][0])
#     result += (lst[max_h_idx][1] - lst[tmp_max_idx][1])
#
#
#
# # result += (lst[j][0] - lst[max_h_idx][0])
# # result += (lst[max_h_idx][1] - lst[j][1])
# #
# #
# #     # if lst[j][1] > lst[j-1][1]:
# #     #     result += (lst[j][0] - lst[max_h_idx][0])
# #     #     result += (lst[max_h_idx][1] - lst[j-1][1])
# #     #     print(result)
#
# print(result)