A, B, V = map(int, input().split())
       
# 마지막 날 A만큼 올랐을 때 V에 도달하면 안 내려가도 되기 때문에
# 우선 V에서 A를 뺀 값을 기준으로 생각
# 그 값에서 A-B가 하루동안 올라가는 미터 수이기 때문에 나눠줌
if (V-A) % (A-B) == 0:                # 만약 값이 정수라면 마지막에 A만큼만 더 올라가면 되기 때문에
    result = ((V-A)//(A-B)) + 1   # A만큼 더 올라가는 날까지 고려하여 + 1
else:                       # 소수값이 존재한다면 그만큼 올라가기 위해 하루가 더 필요하기 때문에 +2
    result = ((V-A)//(A-B)) + 2
print(result)


# 제일 처음에 while 끄적이다가 시간 제한이 0.25초길래 아니겠구나 하고 연산으로 접근
# # result = (V-A) // (A-B) + 1
### 처음에 이렇게 생각했었는데 몫이 나눠떨어지는 경우와 아닌 경우 구분해야 함





# result = (V-A) 
# print(result)


# now = 0
# cnt = 0
# while True:
#     now += A
#     if now >= V:
#         break
#     now -= B
#     cnt += 1
# print(cnt)


# while True:
#     cnt = V // (A-B)
#     if (A-B) * cnt + A >= V:
#         # cnt -= 1
#         break
# print(cnt)
