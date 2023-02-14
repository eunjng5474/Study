N = int(input())
ai = list(map(int, input().split()))
stack = []
stack_lst = []






# stack.append(ai[0])
# for i in range(len(ai)):

for i in range(N):
    if len(stack) == 0:
        stack.append(ai[i])
    for j in range(i+1, N):
        if ai[j] > stack[-1]:
            stack.append(ai[j])
        print(stack)
    stack_lst.append(stack)



# i = 0
# while i < N:
#     if len(stack) == 0:
#         stack.append(ai[i])
#     elif ai[i] > stack[-1]:
#         stack.append(ai[i])
#     stack_lst.append(stack)
#     # stack = []
#     i += 1

print(stack_lst)
result = 0
for s in stack_lst:
    if len(s) > result:
        result = len(s)
print(len(s))    ### 최대값 출력하기


# i = 1
# for j in range(i+1, len(ai)):
#     if ai[j] > stack[-1]:
#         stack.append(ai[j])
#     i += 1
# stack_lst.append(stack)

    # if i == 0:
    #     stack.append(ai[i])

    # if ai[i] > stack[-1]:
    #     stack.append(ai[i])
    # else:
    #     stack_lst.append(stack)
    #     stack = []
    #     stack.append(ai[i])

# print(stack)
# print(stack_lst)

# print(len(stack))    ### 최대값

##### 0부터 끝까지 스택에 넣고 그걸 스택리스트에 넣고
## 그다음 1부터 끝까지, 2부터 , ...


# ### '가장 긴' 빼먹은 코드
# N = int(input())
# ai = list(map(int, input().split()))
# stack = []

# stack.append(ai[0])
# for i in range(1, len(ai)):
#     if ai[i] > stack[-1]:
#         stack.append(ai[i])

# print(len(stack))

