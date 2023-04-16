import sys
sys.stdin = open('input.txt')

def search(txt):
    global result
    for i in range(100):
        for j in range(100):
            for k in range(100):
                tmp = txt[i][j:j+k]
                if tmp == tmp[::-1]:
                    if len(tmp) > result:
                        result = len(tmp)

for t in range(10):
    tc = int(input())
    txt = [input() for _ in range(100)]
    result = 0

    search(txt)

    txt_trans = []
    for i in range(100):
        tmp = ''
        for j in range(100):
            tmp += txt[j][i]
        txt_trans.append(tmp)

    search(txt_trans)
    print(f'#{tc} {result}')
