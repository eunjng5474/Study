N, M = map(int, input().split())
nums = sorted(list(set(map(int, input().split()))))     # 중복 제거
result = []
lst = [0]       # n, m >= 1이므로 비교할 초기값 0으로 설정

def sol(n):
    if len(lst) == M+1:
        print(*lst[1:])     # 0을 제외한 lst의 길이가 M이면 lst의 1번째부터 프린트
        return
        # tmp = sorted(list(lst))
        # if tmp not in result:
        #     result.append(tmp)
        # return
    else:
        for i in range(len(nums)):
            if lst[-1] <= nums[i]:      # 리스트의 가장 마지막 값보다 크거나 같은 경우만 lst에 추가
                lst.append(nums[i])
                sol(i + 1)
                lst.pop()

sol(1)
#
# answer = []
# for i in result:
#     if sorted(i) not in answer:
#         answer.append(sorted(i))
#     else:
#         pass
#
# for a in result:
#     print(*a)
