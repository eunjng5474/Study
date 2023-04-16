mushroom = [int(input()) for _ in range(10)]

result = 0
for m in mushroom:
    if result + m > 100:        # 다음 값 더했을 때 100이 넘는다면
        if ((result+m) - 100) <= (100-result):  # (100-현재) 보다 (다음 m 더한값 - 100)이 작거나 같을 때 result += m
            result += m
            break
        else:                   # 만약 다음 m을 더했을 때 100과의 편차가 현재 값과 100과의 편차보다 크면 안 더하고 break
            break
    result += m
    if result == 100:
        break

print(result)