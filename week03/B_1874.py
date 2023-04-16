
N = int(input())
num_lst = []        # 입력값 넣을 리스트
stack = []

result_lst = []     # + - 넣을 결과 리스트
pop_lst = []        # pop되는 값들을 넣을 리스트
for i in range(N):
    # num = list(map(int, sys.stdin.readline().rstrip()))
    num_lst.append(int(input()))

ver_num = 0         # 1부터 오름차순이므로 비교 숫자는 우선 0
for n in num_lst:
    if n >= ver_num:        # 만약 입력값이 비교 넘버보다 크면
        for i in range(ver_num+1, n+1): # 비교숫자+1부터 n까지 stack에 push
            stack.append(i)
            result_lst.append('+')      # push 했으니 결과 리스트에 + 추가

        p = stack.pop()         # push 끝났으니까 pop하고
        pop_lst.append(p)       # pop된 값을 pop리스트에 추가
        result_lst.append('-')  # pop 했으니 결과 리스트에 - 추가
        ver_num = n             # n 이후부터 다시 비교하기 위해 비교넘버는 n으로 바꾸기

    else:
        p = stack.pop()         # 만약 n이 현재 비교 숫자보다 작으면 바로 pop
        pop_lst.append(p)
        result_lst.append('-')
    # if not stack:             # 처음에 break 조건 넣어줘야 하나 했는데
    #     break                 # 모든 수행이 종료된 후 리스트끼리 비교할거라 제외

if num_lst != pop_lst:          # 만약 num_lst != pop_lst라면
    print('NO')                 # 불가능한 경우
else:   
    for r in result_lst:        # 같으면 가능한 경우이므로 결과 리스트의 모든 값을 한 줄씩 출력
        print(r)
    
    # try:              ### 처음에 try, except로 시도했었으나 실패
    # except:          
    #     print('NO')



### + - 출력되다가 NO가 출력되지 않게 하기 위해서 리스트에 다 추가하고
# 모든 수행이 끝난 뒤 비교하는 방식으로 했는데
# 리스트가 너무 많아서,,, 다른 방법이 있으려나      
