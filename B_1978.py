n = int(input())

n_li = list(map(int, input().split()))
cnt = len(n_li)

for i in n_li:
    if i == 1:
        cnt -= 1
    else:
        for j in range(2, i):
            if i % j == 0:
                cnt -= 1
                break
print(cnt)

# cnt를 리스트의 길이로 지정한 후
# 리스트 내부 값 i에 대해 2부터 i 전까지 범위 내에서 순회하면서
# 만약 한번이라도 j를 나눈 나머지가 0이 되면 소수가 아니므로
# cnt -= 1하고, 약수가 여러 개인 경우 중복 차감되지 않게 하기 위해 break