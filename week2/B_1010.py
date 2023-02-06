T = int(input())

# def fac(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fac(n-1)

for tc in range(T):
    N, M = map(int, input().split())
    n_lst = [0] * N
    m_lst = [1] * M
    # for n in range(N):
    #     a = fac(M-N+1)
    #     b = fac()