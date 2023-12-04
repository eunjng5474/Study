# # 2557
# print('hello world!')

# # 1000
# A, B = map(int, input().split())
# print(A + B)

# # 10869
# A, B = map(int, input().split())
# print(A + B)
# print(A - B)
# print(A * B)
# print(A // B)
# print(A % B)

# # 10926
# id = input()
# print(f'{id}??!')

# # 18108
# year = int(input())
# print(year - 543)

# # 3003
# k, q, r, b, n, p = map(int, input().split())
# print(1-k, 1-q, 2-r, 2-b, 2-n,8-p)

# # 10430
# a, b, c = map(int, input().split())
# print((a+b)%c)
# print(((a%c)+(b%c))%c)
# print((a*b)%c)
# print(((a%c)*(b%c))%c)




# # 2588 곱셈
# a = int(input())
# b = list(map(int, input()))
# c1 = a * b[2]
# c2 = a * b[1]
# c3 = a * b[0]
# print(c1)
# print(c2)
# print(c3)
# print(c1 + c2*10 + c3*100)

# # # 2588 - 2
# # c = []
# # for i in range(len(b), 0, -1):      #len(b)는 생각했는데 range는 기존 SWEA 코드 보고 인지함. 역순 진행은 구글링해서 알아냄
# #     c[i-1] = a * b[i-1]       # b[i]가 아닌 b[i-1]!!
# #     print(c[i])
# # print(c[2] + c[1]*10 + c[0]*100)

# ### 구글링으로 알아낸 코드
# a = int(input())
# b = input()         # b는 각 자릿수별로 구분할 거라 문자열로 입력!!!
# for i in range(len(b), 0, -1):
#     print(a * int(b[i-1]))      # b는 현재 문자열이기 때문에 int()
# print(a * int(b))               # 최종답은 int(a)*int(b)이기 때문




# 10171 고양이
print("\\    /\\")
print(" )  ( ')")
print("(  /  )")
print(" \\(__)|")
## '(따옴표)를 출력하려면 따옴표 포함 텍스트를 " "로 감싸기
## \(백슬래시)를 출력하려면 그 앞에 \ 추가 입력

print("""
\\    /\\
 )  ( ')
(  /  )
 \\(__)|
""")
## """ (텍스트 여러 줄) """ 가능 -> 근데 왜 백준에선 안 되지,,?



# 10172 개
print('|\\_/|')
print('|q p|   /}')
print('( 0 )"""\\')
print('|"^"`    |')
print('||_/=\\\\__|')       ## "(쌍따옴표)를 텍스트로 넣으려면 ' '로 감싸기



# 25083 새싹
print('         ,r\'\"7')
print('r`-_   ,\'  ,/')
print(' \\. ". L_r\'')
print('   `~\\/')
print('      |')
print('      |')
## ', ", \ 앞에 \ 넣어주면 문자로 인식