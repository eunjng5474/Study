N = int(input())
nums = list(map(int, input().split()))
operator = list(map(int, input().split()))
calcul = ['+', '-', '*', '//']
used = [0] * 4

max_sum = -int(1e9)
min_sum = int(1e9)
cal = []

def calculator(lst):
    global max_sum, min_sum
    tmp = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == '+':
            tmp += lst[i+1]
        if lst[i] == '-':
            tmp -= lst[i+1]
        if lst[i] == '*':
            tmp *= lst[i+1]
        if lst[i] == '//':
            if tmp < 0:
                ans = -tmp // lst[i+1]
                tmp = -ans
            else:
                tmp //= lst[i+1]

    if tmp > max_sum:
        max_sum = tmp
    if tmp < min_sum:
        min_sum = tmp
    return


### 중복 제거로 가지치기 더 해주고 싶었는데 리스트에 추가해서 not in 쓰는 거 말고
### 다른 방법 없나,,, 일단 이렇게도 패스긴 함
def sol(i):
    global cal
    cal.append(nums[i])     # 숫자는 중복 없이 연산자보다 먼저 추가되어야 함

    if i == N-1:
        calculator(cal)
        return

    for o in range(4):
        if operator[o] and used[o] != operator[o]:
            cal.append(calcul[o])
            used[o] += 1
            sol(i+1)       # 재귀 호출할 때 다음 숫자 추가하도록 i+1
            used[o] -= 1
            cal.pop()       # 연산자랑 숫자 두 번 pop
            cal.pop()


sol(0)
print(max_sum)
print(min_sum)


# for d in range(N):
# for c in range(4):

