N = int(input())
seat = input()
result = ['*']

i = 0
while i < N:                # 컵홀더 *로 표시
    if seat[i] == 'S':
        result.append('S')
        result.append('*')
        i += 1
    elif seat[i] == 'L' and seat[i+1] == 'L':
        result.append('L')
        result.append('L')
        result.append('*')
        i += 2

cnt = 0
for i in range(1, len(result)):
    if result[i] == 'S' or result[i] == 'L':    # 좌석일 때
        if result[i-1] == '*':      # 왼쪽에 컵홀더 있으면
            cnt += 1                # cnt += 1하고 사용했다는 표시로 '/'로 변경
            result[i-1] = '/'
        elif result[i+1] == '*':    # 왼쪽에 없으면 오른쪽 사용
            cnt += 1
            result[i+1] = '/'

print(cnt)