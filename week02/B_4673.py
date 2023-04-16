# def d(n):
#     nl = len(str(n))
#     result_n = n
#     while True:
#         result_n += n // 10**(nl-1)
#         n = n % 10**(nl-1)
#         if len(str(n)) == 1:
#             break
#     # return d(result_n)
#     return result_n


def d(n):
    nl = len(str(n))            # nl = n의 자릿수
    res_n = n
    for i in range(nl):             # n의 자릿수만큼 순회하면서
        res_n += int(str(n)[i])     # n을 str으로 바꿔서 각 자릿수를 다시 int로 변환해서 res_n에 더하기
    return res_n                    # res_n은 생성자




non_self_num_lst = []                   # 셀프넘버가 아닌 숫자(생성자)들을 담을 빈 리스트 생성
for i in range(1, 10001):               # 1부터 10000까지에 대해서
    result_i = d(i)                     # 함수 실행시킨 값을 저장해서 리스트에 추가
    non_self_num_lst.append(result_i)

for j in range(1, 10001):               # 해당 리스트에 없는 값들 출력
    if j not in non_self_num_lst:
        print(j)



        # for i in range(len(str(n))):                    # 두 자리일 때는 가능할 듯
        # # n = n + (n//(10**(i-1))) + (n%(10**(i-1)))  # for문이 아니라 바꿔야할 듯?
        # # ... n//100 + n//10 + n%10
        #     n += n//(10**i) 
        #     n += (n%(10**(i-1)))