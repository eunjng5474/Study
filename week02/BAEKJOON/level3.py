# # 2739 구구단
# N = int(input())
# for i in range(1, 10):
#     print(f'{N} * {i} = {N*i}')

# i = 1
# while i < 10:
#     print(f'{N} * {i} = {N*i}')
#     i += 1


# # 10950 A+B-3 
# T = int(input())
# for i in range(1, T+1):
#     a, b = map(int, input().split())
#     print(a + b)


# # 8393 합
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)

# i = 1
# sum = 0
# while i < n+1:
#     sum += i
#     i += 1
# print(sum)



# # 25304 영수증
# X = int(input())
# N = int(input())
# sum_p = 0
# i = 1
# for i in range(N):
#     a, b = map(int, input().split())
#     sum_p += a * b
# if sum_p == X:
#     print('Yes')
# else:
#     print('No')

# # while i < N+1:
# #     a, b = map(int, input().split())
# #     sum_p += a * b
# #     i += 1



# # 15552 빠른 A+B
# import sys

# T = int(input())
# for i in range(T):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a + b)



# # 11021 A+B - 7
# T = int(input())
# for i in range(1, T+1):
#     a, b = map(int, input().split())
#     print(f'Case #{i}: {a+b}')



# # 11022 A+B - 8
# T = int(input())
# for i in range(1, T+1):
#     a, b = map(int, input().split())
#     print(f'Case #{i}: {a} + {b} = {a+b}')



# # 2438 별 찍기 1
# N = int(input())
# for i in range(1, N+1):
#     print('*'*i)



# # 2439 별 찍기 2
# N = int(input())
# # for i in range(1, N+1):
# #     print(' '*(N-i), '*'*i)         # 공백이 +1임,,, why??

# for i in range(N):
#     print(' '*(N-i-1) + '*'*(i+1))



# # 10952 A+B - 5
# a, b = map(int, input().split())
# while a != 0 or b != 0:
#     print(a+b)
#     a, b = map(int, input().split())



# # 10951 A+B - 4             ## 구글링 해서 품
# while True:
#     try:
#         a, b = map(int, input().split())
#     except:
#         break
#     print(a+b)



# 1110 더하기 사이클
N = int(input())
num = N
cnt = 0
while True:
    a = num // 10
    b = num % 10
    # sum = a + b
    c = (a + b) % 10            # 구글링
    num = b * 10 + c            # 구글링
    # print(num)      # 26 - 68 - 84 - 42 - 26
    cnt += 1

    if num == N:        # 구글링
        break

print(cnt)
    

# sum1 = (N // 10) + (N % 10)
# sum2 = ((N%10 + sum1%10) // 10) + ((N%10 + sum1%10) % 10) 

# m1 = (N % 10) + (sum1 % 10)
# m1 = 'n2' + 'sum1 % 10'
# sum2 = (m1 // 10) + (m1 % 10)

# if N < 10:
    # N = '0'+N
# print(N)
# print(type(N))


# n1 = N[0]
# n2 = N[1]
# sum1 = int(n1) + int(n2)
# sum2 = int(n2) + int(str(sum1)[1])
# sum3 = int(str(sum1)[1]) + int(str(sum2)[1])

# for i in range(2):
#     sum1 = N[i]

# int(N[0]) + int(N[1]) = sum1
# int(N[1]) + sum1[1] = sum2
# # N[2] + sum1[]
# for i in range(2):
#     sum_1 = N