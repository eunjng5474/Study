n,k = map(int, input().split())
lst = list(range(2, n+1))       # 2부터 n까지의 숫자를 리스트로 만들고
result_li = []                  # 지워지는 값 담을 빈 리스트 생성
# print(lst)
# result_dict[1] = lst.pop(0)

# print(result_dict)

i = 1
while i <= n:                   # i는 1부터 시작해서 n까지 반복문 순회
    # for i in range(1, n+1):
    p = lst.pop(0)              # 리스트의 첫번째 값을 제거하고 제거되는 값을 p로 저장
    result_li.append(p)         # 결과 리스트에 p 추가

    for j in range(1, (n//p+1)):        # 1부터 n//p까지의 값 j에 대해
        try:
            lst.remove(p * j)           # p * j (p의 배수)가 있으면 해당 값을 제거하고
            result_li.append(p * j)     # 결과 리스트에 추가
        except:                         # 예외처리(p의 배수가 없으면)
            i += 1                      # i += 1해서 반복문 다시 순회
    if not lst:                         # 만약 lst가 모두 비어서 False가 된다면 break
        break

# print(result_li)

print(result_li[k-1])                   # 결과 리스트에서 k번째 값 반환