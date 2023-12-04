# 1936 - 0. 1대1 가위바위보
## 처음에 이렇게 제출했었는데 생각해보니 가위(1)가 보(3)를 이기는 경우 고려 안 함
a, b = input().split()
a = int(a)
b = int(b)

if a > b:
    print("A")
elif a < b:
    print("B")


# 1936 - 1
## 그래서 모든 케이스 적용 가능하도록 수정
a, b = map(int, input().split())

if a == 1:
    if b == 2:
        print('B')
    elif b == 3:
        print('A')
elif a == 2:
    if b == 1:
        print('A')
    elif b == 3:
        print('B')
elif a == 3:
    if b == 1:
        print('B')
    elif b == 2:
        print('A')


# 1936 -2
## 코드가 너무 길어서 명료하게 수정
if a - b == 1 or a - b == -2:
    print('A')
elif b - a == 1 or b - a == -2:
    print('B')




# 2058 자릿수 더하기
n = input()
n = list(map(int, str(n)))
answer = 0

for i in range(len(n)):
    answer += n[i]
print(answer)
## str -> int -> list
## n의 길이(6789의 경우 4) 내에서 0~3 모두 더하기 





# 2063 중간값 찾기
N = int(input())
score = list(map(int, input().split()))
score.sort()

index = (N-1)//2
median = score[index]
print(median)
# 처음에 전체 개수인 N을 입력받고
# N개의 값들을 입력 받아서 list로 만들어 정렬하고 N은 홀수이므로 (N-1)//2 번째 값이 중간값 
# 처음에 잘못 생각해서 `index = N//2 + 1`로 했다가 output이 58이 아닌 59가 나왔었다.
# 홀수의 경우 (n-1)//2 




# 2068 최대수 구하기
T = int(input())

for i in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print(f"#{i} {max(numbers)}")
# test 개수 입력 받아서 T로 할당하고
# list는 0부터 시작이지만 테스트 케이스의 번호를 1부터 시작하게 하기 위해 range를 1부터 T+1로 설정
# 테스트 케이스 값 받으면 그 중 max출력하고, 그 앞에 #i로 테스트 케이스 번호 출력
# 이 때 f를 ' '앞에 적거나 뒤에 .format으로도 가능
### print("#{} {}".format(i, max(numbers)))



# 2071 평균값 구하기
T = int(input())

for i in range(1, T + 1):
    numbers = list(map(int, input().split()))
    print(f"#{i} {round(sum(numbers)/len(numbers))}")
# 2068번 최대수 구하기와 비슷!
# 하지만 평균값을 구하기 위해 numbers의 각 값들을 모두 더하고 값의 개수(len(numbers))로 나누기
# 이 때 처음부터 //를 통해 정수값으로 나오게 하는 것이 아니라
# 소수점 첫째 자리에서 반올림한 정수를 출력하는 것이기 때문에
# /를 통해 나눈 후 round 사용