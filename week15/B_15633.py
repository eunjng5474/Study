n = int(input())
sum = 0
for i in range(1, n+1):
    if not n % i:
        sum += i
print(sum*5 - 24)