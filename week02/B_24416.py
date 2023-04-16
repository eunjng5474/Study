def fib(n):
    cnt = 0
    if n == 1:
        cnt += 1
        return cnt
    elif n == 2:
        cnt += 1
        return cnt
    else:
        cnt += 1
        return fib(n-1) + fib(n-2)
# 문제에서 제시한 의사 코드 참고해서 cnt 반환하도록 수정

def fibonacci(n):
    fibo = [0] * (n+1)
    fibo[1] = 1
    fibo[2] = 1
    cnt = 0
    for i in range(3, n+1):
        fibo[i] = fibo[i-1] + fibo[i-2]
        cnt += 1
    return cnt
# dp 설명 및 구글링 코드 참고 후 스스로 작성 및 수정하며 이해


n = int(input())

result1 = fib(n)
result2 = fibonacci(n)
print(result1, result2)
