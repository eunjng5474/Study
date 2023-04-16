# ### sol1 - 시간 초과일 거 같긴 했는데 진짜 시간 초과,,,

# import sys

# N = int(input())
# have = list(map(float, sys.stdin.readline().split()))
# M = int(input())
# check = list(map(float, sys.stdin.readline().split()))

# for c in check:
#     if c in have:
#         result = 1
#     else:
#         result = 0
#     print(result, end=' ')


### sol2
import sys

N = int(input())
h_lst = list(map(float, sys.stdin.readline().split()))
have = sorted(h_lst)
M = int(input())
c_lst = list(map(float, sys.stdin.readline().split()))

for c in c_lst:
    start = 0
    end = N-1

    while True:
        middle = (start + end) // 2
        if c == have[middle]:
            print(1, end=' ')
            break
        elif c < have[middle]:
            end = middle - 1
        elif c > have[middle]:
            start = middle + 1

        if start > end:
            print(0, end=' ')
            break
        
## 질문게시판 보고 이진 검색 사용해야 한다는 걸 알게됨
## 순차 검색 시간 복잡도: O(N)
## 이진 검색 시간 복잡도: O(logN)
