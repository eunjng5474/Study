t = int(input())

for i in range(t):
    n1, n2 = map(int, input().split())
    a, b = n1, n2
    while True:
        nn = a % b
        a, b = b, nn
        if nn == 0:
            max_n = a
            break
    rest_a = n1 // max_n
    rest_b = n2 // max_n
    print(max_n * rest_a * rest_b)

# 2609와 같은 방식 사용