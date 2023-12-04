# # 1330 두 수 비교하기

# a, b = map(int, input().split())        # 처음에 int(input().split()) 했다가 error
# if a > b:
#     print('>')
# elif a < b:
#     print('<')
# else:
#     print('==')


# # 9498 시험 성적
# score = int(input())
# if score >= 90:
#     print('A')
# elif score >= 80:
#     print('B')
# elif score >= 70:
#     print('C')
# elif score >= 60:       # 처음에 elif >= n0: 으로 했다가 error
#     print('D')
# else:
#     print('F')



# # 2753 윤년
# year = int(input())
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print('1')
# else:
#     print('0')



# # 14681 사분면 고르기
# x = int(input())
# y = int(input())
# if x > 0:
#     if y > 0:
#         print('1')
#     else:
#         print('4')
# else:
#     if y > 0:
#         print('2')
#     else:
#         print('3')

        

# # 2884 알람 시계
# h, m = map(int, input().split())
# if m >= 45:
#     print(f'{h} {m-45}')
# else:
#     if h == 0:
#         h += 24
#     print(f'{h-1} {m+60-45}')



# # 2525 오븐 시계
# h, m = map(int, input().split())
# t = int(input())
# t_h = t // 60
# t_m = t % 60
# if m + t_m >= 60:         # 이 부분 놓치지 말기!
#     h += 1
#     m -= 60
# if h + t_h < 24:
#     print(f'{h + t_h} {m + t_m}')
# else:
#     print(f'{(h + t_h)-24} {m + t_m}')



# 2480 주사위 세개
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a*1000)
elif a == b or a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
else:
    print(max(a, b, c)*100)
### 더 간단하게 가능할 것 같은데,,,