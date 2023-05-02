import sys
input = sys.stdin.readline

M = int(input())
s = set()
for m in range(M):
    i = input().rstrip().split()
    if len(i) == 1:
        if i[0] == 'all':
            s = set([k for k in range(1, 21)])
        else:
            s = set()
        continue

    if i[0] == 'add':
        s.add(int(i[1]))
    elif i[0] == 'remove':
        s.discard(int(i[1]))
        # remove 대신 discard 쓰면 set 안에 해당 값 없어도 에러 안 나고 정상 작동

    elif i[0] == 'check':
        if int(i[1]) in s:
            print(1)
        else:
            print(0)

    elif i[0] == 'toggle':
        if int(i[1]) in s:
            s.discard(int(i[1]))
        else:
            s.add(int(i[1]))
