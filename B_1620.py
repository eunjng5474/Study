### sol 1 -> 시간 초과
# n, m = map(int, input().split())

# n_list = []
# for i in range(n):
#     n_list.append(input())
# # n_list = enumerate(n_list)

# # print(n_list[1])
# for j in range(m):
#     a = input()
#     for idx, name in enumerate(n_list, start=1):
#         if a.isdigit() == True and int(a) == idx:     # isdigit() 구글링
#             print(name)
#         elif a == name:
#             print(idx)



### sol 2 -> 시간 초과. 리스트에 다 추가해서 비교하는 방식 말고 다른 방식 찾기
        
# import sys

# n, m = map(int, input().split())
# n_list = []
# for i in range(n):
#     n_in = sys.stdin.readline().rstrip()
#     n_list.append(n_in)

# for j in range(m):
#     a = sys.stdin.readline().rstrip()
#     for idx, name in enumerate(n_list, start=1):
#         if a.isdigit() == True and int(a) == idx:
#             print(name)
#         elif a == name:
#             print(idx)




### sol 3


import sys

n, m = map(int, input().split())
int_dic = {}
name_dic = {}
for i in range(1, n+1):
    n_in = sys.stdin.readline().rstrip()
    int_dic[i] = n_in
    name_dic[n_in] = i

for j in range(m):
    a = sys.stdin.readline().rstrip()
    if a.isdigit() == True:
        print(int_dic[int(a)])
    else:
        print(name_dic[a])

# isdigit() 메서드도 구글링 통해서 알았음
# sys 사용은 질문 게시판에서 확인 후 구글링 통해 사용
# 처음에 딕셔너리 하나만 만들었다가 value로 key값 불러올 수 없어서
# key가 각 int / name인 딕셔너리 두 개 생성







#     li = sys.stdin.


        # if a == name:
        #     print(idx)
        # elif int(a) == idx:
        #     print(name)
        # print(n_list[int(a)])
        # if n_list[name] == a:
        #     print(idx)
        # elif int(a) == idx:
        #     print(n_list[idx])
        # if a in n_list[idx]:
        #     print(idx + 1)
        # elif int(a) in n_list[idx]:
        #     print(name)

    # if a in enumerate(n_list):
        # print(idx + 1)
