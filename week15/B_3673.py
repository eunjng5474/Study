C = int(input())
for tc in range(C):
    d, n = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0

    mod = [0] * d
    sum_n = 0

    for num in nums:
        # sum에 현재 숫자 더하기
        sum_n += num
        # 나머지만 계산
        sum_n = sum_n % d

        # 현재의 나머지에서 동일한 나머지의 값을 빼면 나머지가 0이 되어 d의 배수가 된다.
        # 따라서 mod에서 해당 인덱스에 저장된 개수만큼 cnt에 추가
        # 즉, 나머지가 같은 경우가 mod에 저장되어 있으므로 그만큼의 개수가 추가됨
        cnt += mod[sum_n]
        # cnt에 계산한 다음 현재 누적합에 대해 mod에 += 1
        mod[sum_n] += 1

    # 나머지가 0인 경우도 더해주기
    cnt += mod[0]
    print(cnt)




#### 시간초과
    # for dd in range(d, sum(nums)+1, d):
    #     sum_n = 0
    #     left = 0
    #     right = 0
    #     while True:
    #         if sum_n >= dd:
    #             if sum_n == dd:
    #                 cnt += 1
    #             sum_n -= nums[left]
    #             left += 1
    #         if right == n:
    #             break
    #         else:
    #             sum_n += nums[right]
    #             right += 1
    # print(cnt)

