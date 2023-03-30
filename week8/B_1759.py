import sys
input = sys.stdin.readline

def check(lst):
    v = 0
    c = 0
    for i in lst:
        if i in 'aeiou':    # 모음 개수 확인
            v += 1
        else:               # 자음 개수 확인
            c += 1
    if v >= 1 and c >= 2:   # 조건 충족 시 True
        return True
    else:
        return False

def sol(n):
    if len(lst) == L:
        flag = check(lst)   # 조건 충족 여부 확인
        if not flag:
            return

        for l in lst:
            print(l, end='')
        print()
        return

    for i in range(n, C):
        lst.append(alphabet[i])
        sol(i+1)
        lst.pop()


L, C = map(int, input().split())
alphabet = sorted(list(input().split()))
lst = []
sol(0)
