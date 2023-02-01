n = int(input())

# for i in range((n//3)+1, 0, -1):
#     if (n - (5*i)) > 0 and (n - (5*i)) % 3 == 0:
#         a = (n - (5*i)) // 3
#         print(a + i)
#         break
#     elif n % 5 == 0:
#         print(n // 5)
#         break
#     elif n % 3 == 0:
#         print(n // 3)
#         break
# else:
#     print(-1)


a = b = 0
for i in range((n//3)+1, 0, -1):        # i는 (n을 3으로만 채웠을 때의 몫 + 1)부터 1까지 역순
    if n - (5*i) == 0:                  # 만약 n이 5의 배수라면 5로 나눈 몫 프린트
        b = n // 5                      # 가장 1순위로 계산하기 위해 % 안 쓰고 for문 안에 i로 순환하도록
        print(b)
        break                           # 만약 값이 반환되면 for문 종료
    elif (n - (5*i)) > 0 and (n - (5*i)) % 3 == 0:     
        # n보다 작은 범위 내에서 5의 배수 중 최대값을 뺐을 때 그 나머지가 3의 배수라면
        # i는 큰값부터 점차 줄어들기 때문에 5kg 봉지를 최대로 가지게 됨
        a = (n - (5*i)) // 3            # a는 3kg 봉지 개수
        b = a + i                       # i는 5kg 봉지 개수
        print(b)                        # 프린트는 a + i
        break
if not b and n % 3 == 0:                # for문을 다 돌고나서도 b가 False인데 n이 3의 배수라면
    b = n // 3                          # 3kg 봉지로만 채워서 그 개수 반환
    print(b)
elif not b:                             # 만약 프린트한 값이 없다면(b가 그대로 0으로 False라면) -1 반환
    print(-1)






# if (n % 5) % 3 == 0:
#     a = n // 5
#     b = (n % 5) // 3
#     print(a + b)
# elif (n % 3) % 5 == 0:
#     a = n // 3
#     b = (n % 3) // 5
#     print(a + b)