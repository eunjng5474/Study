n = int(input())
result = n              # 한 변이 1인 사각형 n개
for i in range(2, n):   # 한 변이 2 이상인 사각형
    for j in range(i, n//i+1):      # i부터 n//i까지 개수 더하기
        # (6의 경우 한 변이 2인 사각형이 2*2, 2*3)
        # 범위를 i부터 잡아서 중복값 없도록
        result += 1
print(result)