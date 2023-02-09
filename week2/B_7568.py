import sys

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
    

N = int(input())
w_lst = []
h_lst = []
rank_lst = [0] * N
# dc_lst = []

for n in range(N):
    w, h = map(int, sys.stdin.readline().split())
    # dc_lst.append(dc)

    w_lst.append(w)
    h_lst.append(h)

sort_w_lst = sorted(w_lst, reverse=True)
sort_h_lst = sorted(h_lst, reverse=True)


for ww in range(len(w_lst)):                    # w_lst의 값 ww에 대해서
    w_idx = sort_w_lst.index(w_lst[ww])         # 정렬 리스트에서 ww의 인덱스를 찾으면 몸무게의 등수가 됨
    rank_lst[ww] += w_idx                       # 등수 리스트의 ww번째 값에 몸무게의 등수 할당

for hh in range(len(h_lst)):
    h_idx = sort_h_lst.index(h_lst[hh])         # 키에 대해서도 똑같이 적용
    rank_lst[hh] += h_idx  

print(rank_lst)

# for r in rank_lst:              # 이 값을 기준으로 등수로 바꾸면 될 것 같은데,,,,
rank1_idx = rank_lst.index(min(rank_lst))
print(rank1_idx)










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