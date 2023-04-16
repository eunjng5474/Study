import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
string = input()

result = 0
i = 0
cnt = 0

while i < M:
    if string[i:i+3] == 'IOI':
        i += 2      # 두 칸 뒤(두번째 I부터 탐색)
        cnt += 1    # 'IOI' 개수
        if cnt == N:
            result += 1
            cnt -= 1        # 두 칸 뒤부터 다시 cnt == N인지 확인해야하니까
    else:
        i += 1            # 아닌 경우 한 칸 뒤부터 조사. cnt 초기화
        cnt = 0

print(result)


#
# PN = 'IO'*N + 'I'
# p = len(PN)
#
# result = 0
# string = ''
# tmp = ''
# for i in range(M-1):
#     if S[i] != S[i+1]:
#         tmp += S[i]
#     else:
#         # tmp += S[i+1]
#         if len(tmp) > len(string):
#             string = tmp
#
#
# if string[0] != 'I':
#     string.lstrip()
# if string[-1] != 'I':
#     string.rstrip()
# print(string)










# #### 50점 - N,M 커지면 시간초과인 듯
# N = int(input())
# M = int(input())
# S = input()
#
# PN = 'IO'*N + 'I'
# p = len(PN)
#
# result = 0
# for i in range(M-p+1):
#     if S[i:i+p] == PN:
#         result += 1
# print(result)
