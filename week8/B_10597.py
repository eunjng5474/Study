## 구글링
def sol(n):
    if n == len(nums):
        print(*lst)
        exit() # 함수 종료

    # 1자리 수
    num1 = int(nums[n])
    if not visited[num1]:
        visited[num1] = 1
        lst.append(num1)
        sol(n+1)
        visited[num1] = 0
        lst.pop()

    # 2자리 수
    if n+1 < len(nums):
        num2 = int(nums[n:n+2])
        if num2 <= N and not visited[num2]:
            visited[num2] = 1
            lst.append(num2)
            sol(n+2)
            visited[num2] = 0
            lst.pop()


nums = input()
if len(nums) < 10:
    N = len(nums)
else:
    N = 9 + (len(nums)-9)//2
    # 9까지는 모두 한 자리 수이고 그 이후로는 두자리수이기 때문에
    # 한 자리 수 9개 + 두 자리 수 개수: (10부터 시작되는 두자리 수 숫자들)//2

visited = [0] * 51
lst = []
sol(0)