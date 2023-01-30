n, m = map(int, input().split())

n_list = []
for i in range(n):
    n_list.append(input())
# n_list = enumerate(n_list)

# print(n_list[1])
for j in range(m):
    a = input()
    for idx, name in enumerate(n_list, start=1):
        if a.isdigit() == True and int(a) == idx:
            print(name)
        elif a == name:
            print(idx)

### -> 시간 초과
        
import sys

# n, m = map(int, input().split())
# n_list = []
# for i in range(n):
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
