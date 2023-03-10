def solution(numbers):
    answer = 0
    number_lst = sorted(list(map(int, numbers)), reverse=True)
    result = []
    tmp = ''
    for i in range(len(number_lst)):
        tmp += str(number_lst[i])

    n = int(tmp)
    prime = [True] * (n + 1)
    prime[0] = False
    prime[1] = False
    for i in range(2, n + 1):
        if prime[i]:
            for j in range(i * 2, n + 1, i):
                prime[j] = False

    num = ''
    for i in range(len(numbers)):
        num += str(number_lst[i])
        for j in range(len(numbers)):
            if i != j:
                num += str(number_lst[j])


    return answer

num = ''
def make(i):
    global num, number_lst
    # for i in range(len(number_lst)):
    num += str(number_lst[i])
    for j in range(len(number_lst)):
        if i != j:
            make(j)


print(solution('17'))

# def check(n):
#     prime = [True] * (n+1)
#     prime[0] = False
#     prime[1] = False
#     for i in range(2, n+1):
#         if prime[i]:
#             for j in range(i*2, n+1, i):
#                 prime[j] = False
#
# numbers = '011'
# number_lst = sorted(list(map(int, numbers)), reverse=True)
# print(number_lst)