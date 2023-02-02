import sys

# sentence = list(map(str, sys.stdin.readline().split('.')))
# sentence = input().split('.')

sentence =[]
while True:
    b = sys.stdin.readline().split('.')
    if b == '':
        break
    sentence.append(b)

print(sentence)

# for i in sentence:
#     a = sentence.count('(')
#     b = sentence.count(')')
#     c = sentence.count('[')
#     d = sentence.count(']')
#     if a == b and c == d:
#         print('yes')
#     else:
#         print('no')


'''
So when I die (the [first] I will see in (heaven) is a score list).
[ first in ] ( first out ).
Half Moon tonight (At least it is better than no Moon at all].
A rope may form )( a trail in a maze.
Help( I[m being held prisoner in a fortune cookie factory)].
([ (([( [ ] ) ( ) (( ))] )) ]).
 .
.
'''