import sys

N = int(input())
# w_lst = []
# h_lst = []
rank_lst = [1] * N
dc_lst = []

for n in range(N):
    dc = tuple(map(int, sys.stdin.readline().split()))
    dc_lst.append(dc)

    idx_1st = 0
    for i in range(N):
        if dc_lst[i][0] > dc[idx_1st][0] and dc_lst[i][1] > dc[idx_1st][1]:
            rank_lst[idx_1st] += 1
            idx_1st = i
        elif dc_lst[i][0] < dc[idx_1st][0] and dc_lst[i][1] < dc[idx_1st][1]:
            rank_lst[i] += 1
        # else:
        #     if




    # w_lst.append(dc[0])
    # h_lst.append(dc[1])

# max_dc = dc[0]
# rank_lst[0] = 1
# for d in dc: 
#     # if d[0] > max_dc[0] and d[1] > max_dc[1]:
        
# sort_dc_lst = sorted(dc_list, reverse = True)
# if sor

# sort_w_lst = sorted(w_lst)
# sort_h_lst = sorted(h_lst)