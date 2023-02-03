import sys

# sentence = list(map(str, sys.stdin.readline().split('.')))
# sentence = input().split('.')

stack =[]
while True:
    s = sys.stdin.readline().rstrip()
    if s == '.':
        break

    for i in s:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            try:
                stack.remove('(')
            except:
                print('no')
        elif i == ']':
            try:
                stack.remove('[')
            except:
                print('no')    
    if stack:
        print('no')
    else:
        print('yes')







# # print(sentence)

#     for i in s:
#         a = s.count('(')
#         b = s.count(')')
#         c = s.count('[')
#         d = s.count(']')
#         if a == b and c == d:
#             print('yes')
#         else:
#             print('no')


# '''
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .
# '''