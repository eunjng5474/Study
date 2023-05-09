C = int(input())
for tc in range(C):
    d, n = map(int, input().split())
    nums = list(map(int, input().split()))
    cnt = 0

    for dd in range(d, sum(nums)+1, d):
        sum_n = 0
        left = 0
        right = 0
        while right < n:
            if sum_n == dd:
                print(left, right-1, sum_n)
                cnt += 1
            if sum_n >= dd:
                sum_n -= nums[left]
                left += 1


            else:
                sum_n += nums[right]
                right += 1
            # print('dd: ', dd)
            # print(sum_n)
    print(cnt)
    print('-------')
