## 1
dc_lst = []
N = int(input())
rank_lst = []

for n in range(N):
    w, h = map(int, input().split())
    dc_lst.append((w, h))

for i in dc_lst:                # dc_lst의 모든 값 순회
    rank = 1                    # 등수 기본값 1
    for j in dc_lst:
        if i[0] < j[0] and i[1] < j[1]:  # 또 다른 모든 값 순회하면서
            rank += 1                    # w, h 모두 i가 j보다 작으면 i의 등수 + 1 
    rank_lst.append(rank)                # 모든 j 순회 후 i의 등수를 등수 리스트에 추가

print(*rank_lst)

## 처음에 꼬아서 풀다가 도저히 안 되겠어서 구글링 도움 받음,,,
## 브루트 포스 코드 짜는 거에 대해 익숙해지자,,






# ## no_sol : 처음에 너무 꼬아서 생각함   

# import sys   

# N = int(input())
# w_lst = []
# h_lst = []
# sum_rank_lst = [0] * N
# result_rank_lst = [0] * N

# for n in range(N):
#     w, h = map(int, sys.stdin.readline().split())

#     w_lst.append(w)
#     h_lst.append(h)

# sort_w_lst = sorted(w_lst, reverse=True)        ## 시간초과 안 뜨려나,,?
# sort_h_lst = sorted(h_lst, reverse=True)


# for ww in range(len(w_lst)):                    # w_lst의 값 ww에 대해서
#     w_idx = sort_w_lst.index(w_lst[ww])         # 정렬 리스트에서 ww의 인덱스를 찾으면 몸무게의 등수가 됨
#     sum_rank_lst[ww] += w_idx                       # 등수 리스트의 ww번째 값에 몸무게의 등수 할당

# for hh in range(len(h_lst)):
#     h_idx = sort_h_lst.index(h_lst[hh])         # 키에 대해서도 똑같이 적용
#     sum_rank_lst[hh] += h_idx  

# print(sum_rank_lst)

# tmp_rank_lst = sum_rank_lst         ## 이 값을 기준으로 등수로 바꾸면 될 것 같은데,,,,

# while tmp_rank_lst:
#     rank = 1
#     min_r = min(tmp_rank_lst)
#     cnt = tmp_rank_lst.count(min_r)
#     for r in sum_rank_lst:
#         if r == min_r:
#             r_idx = sum_rank_lst.index(r)
#             result_rank_lst[r_idx] = rank
#             tmp_rank_lst.remove(r)
#             print(tmp_rank_lst)
#             print(sum_rank_lst)
#         rank += cnt
# print(result_rank_lst)
        










###############################
# def compare(a, b, N):
#     rank_lst = [1] * N
#     dc_lst = []
#     idx_1st = 0

#     for i in range(N):
#         if a[0] > b[0] and a[1] > b[1]:
#             rank_lst[idx_1st] += 1
#             idx_1st = i
#         elif a[0] < b[0] and a[1] < b[1]:
#             rank_lst[i] += 1
 


#     idx_1st = 0
#     for i in range(N):
#         if dc_lst[i][0] > dc[idx_1st][0] and dc_lst[i][1] > dc[idx_1st][1]:
#             rank_lst[idx_1st] += 1
#             idx_1st = i
#         elif dc_lst[i][0] < dc[idx_1st][0] and dc_lst[i][1] < dc[idx_1st][1]:
#             rank_lst[i] += 1
#         # else:
#         #     if




#     # w_lst.append(dc[0])
#     # h_lst.append(dc[1])

# # max_dc = dc[0]
# # rank_lst[0] = 1
# # for d in dc: 
# #     # if d[0] > max_dc[0] and d[1] > max_dc[1]:
        
# # sort_dc_lst = sorted(dc_list, reverse = True)
# # if sor

# # sort_w_lst = sorted(w_lst)
# # sort_h_lst = sorted(h_lst)