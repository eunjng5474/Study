import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    result = ''
    arr = [list(input()) for _ in range(5)]

    for i in range(15):
        for j in range(5):
            try:
                result += arr[j][i]
            except:
                pass

    print(f'#{tc} {result}')
