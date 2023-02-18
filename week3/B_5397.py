## sol 1 - 시간 초과 떠서 구글링 한 뒤의 풀이
import sys

T = int(input())
for tc in range(T):
    string = sys.stdin.readline().rstrip()  
    left = []       ## 커서 왼쪽 값 리스트
    right = []      ## 커서 오른쪽 값 리스트

    for s in string:
        if s not in '-<>':      # 백스페이스, 화살표가 아니면 왼쪽 리스트에 추가
            left.append(s)
        else:
            if s == '-' and left:   # 백스페이스이고 왼쪽 리스트에 값이 있으면
                left.pop()          # 앞에 입력한 값 지우기
            elif s == '<' and left: # 왼쪽 화살표이고 왼쪽 리스트에 값이 있으면
                tmp = left.pop()    # 왼쪽 리스트의 가장 마지막 값을 오른쪽 리스트로
                right.append(tmp)
            elif s == '>' and right:    # 오른쪽 화살표면 반대로
                tmp = right.pop()
                left.append(tmp)
    left.extend(reversed(right))        # 커서 오른쪽에 있는 값들을 반대로 값들만 left에 추가
    print(''.join(left))




# #### sol 2 - 처음 풀이
import sys

T = int(input())
for tc in range(T):
    string = sys.stdin.readline().rstrip()
    stack = []
    tmp = []
    # result = ''
    
    for s in string:
        if s not in '-<>':
            stack.append(s)
        else:
            if s == '-' and stack:
                stack.pop()
            elif s == '<' and stack:
                tmp_s = stack.pop()
                tmp.append(tmp_s)
            elif s == '>' and tmp:
                tmp_s = tmp.pop()
                stack.append(tmp_s)
    stack.extend(reversed(tmp))   
    print(''.join(stack))


    # while stack:
    #     result += stack.pop()
    # print(result[::-1])
    #### 이거때문에 시간 초과였고 위 방식으로 출력하면 패스