T = int(input())

for tc in range(T):
    stack = []
    ps = input()
    
    for n in ps:
        if n == '(':
            stack.append(n)
        elif n == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                stack.append(n)
    
    if not stack:
        print('YES')
    else:
        print('NO')