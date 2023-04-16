T = int(input())
for i in range(T):
    txt = input()
    result = 0

    cnt = 0
    for i in range(len(txt)):
        if txt[i] == 'O':
            cnt += 1
        else:
            for j in range(cnt+1):
                result += j
                cnt = 0
    for j in range(cnt + 1):
        result += j
    print(result)



###########
    # for i in range(len(txt)-1):
    #     if txt[i] == 'O':
    #         tmp = 1
    #         if txt[i+1] == 'O':
    #             tmp += 1
    #     else:
    #         tmp = 0
    #     #     for j in range(tmp):
    #     #         result += j
    #     #         # tmp = 0
    #     # for j in range(tmp):
    #     #     result += j
    #     print(tmp)
    #     result += tmp
    # print(result)
    # print()
    #
    # recent_x = -1
    # for i in range(len(txt)):
    #     if txt[i] == 'X':
    #         for j in range(recent_x+1, i):
    #             result += j
    #         recent_x = i
    #
    # print(result)
