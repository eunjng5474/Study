n = int(input())

# n_lst = []

def func(num):
    for i in range(2, num+1):
        if num % i == 0 and num//i == 1:
            return i
        elif num % i == 0:
            print(i)
            return func(num//i)
            
    # elif n == 1:
    # print('')

print(func(n))




## sol 2
# while n 