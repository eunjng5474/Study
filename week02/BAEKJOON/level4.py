# # 10807 개수 세기

# n = int(input())
# n_list = list(map(int, input().split()))
# v = int(input())
# print(n_list.count(v))  # 구글링

# # v_dict = {}
# # for num in n_list:
# #     if num in v_dict:
# #         v_dict[num] += 1
# #     else:
# #         v_dict[num] = 1
# # print(v_dict)

# # v = int(input())
# # if v in v_dict:
# #     print(v_dict[v])
# # else:
# #     print(0)



# # 10871 x보다 작은 수
# n, x = map(int, input().split())
# n_list = list(map(int, input().split()))
# for num in n_list:
#     if num < x:
#         print(num, end = ' ')



# # 10818 최소, 최대
# n = int(input())
# n_list = list(map(int, input().split()))
# print(min(n_list), max(n_list), end = ' ')



# # 2562 최댓값
# n_list = []
# for i in range(9):
#     num = int(input())
#     n_list.append(num)
# # # n_list = enumerate(n_list)
# # # print(n_list)
# # # print(max(n_list))

# # # print(max(n_list))
# # # if n_list[id] == max(n_list):
# # #     print(id)

# # # print(max(n_dic[idx]))
# # # if n_dic[idx] == max(n_dic[idx]):
# #     # print(idx)


# for idx, num in enumerate(n_list):      # 교재 보고 enumerate 사용
#     n_max = max(n_list)
#     if n_list[idx] == n_max:
#         print(n_max)
#         print(idx + 1)


# # n_max = max(n_list)               # 숏코딩 참고
# # idx = n_list.index(n_max) + 1
# # print(n_max)
# # print(idx)



# # 5597 과제 안 내신 분..?
# x_list = []
# for i in range(28):
#     x_list.append(int(input()))
# # print(x_list)
# # x_list = sorted(x_list)
# # print(x_list)
# for j in range(1, 31):
#     if j not in x_list:
#         print(j)



# # 3052 나머지
# a_li = []
# b_dic = {}
# for i in range(10):
#     a_li.append(int(input()))
# for j in a_li:
#     try:                    # try 사용하는 거 구글링 통해 알아냄
#         b_dic[j % 42] += 1
#     except:
#         b_dic[j % 42] = 1
#     # if b_dic[j % 42] in b_dic:
#     # b_dic[j % 42] = 1
#     # else:
#         # b_dic[j % 42] = 1
# print(len(b_dic))



# # 1546 평균
# n = int(input())
# scores = list(map(int, input().split()))
# m = max(scores)
# new_sc = []
# for i in scores:
#     new_sc.append((i/m*100))
# print(sum(new_sc) / len(new_sc))



# 8958 ox퀴즈
t = int(input())
o_list = []
for i in range(t):
    t_case = input()
    x_cnt = t_case.count('X')
    for j in range(x_cnt):
        pass

