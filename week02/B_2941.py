string = input()
cnt = 0
ca_lst = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
# 글자 수가 다른 'dz=' 제외한 나머지 알파벳들을 리스트화

while string:
    if string[0:3] == 'dz=':                        
        # 글자수가 가장 긴(3글자) 'dz='와 비교해서 일치하면
        cnt += 1
        string = string.replace(string[0:3], '', 1) # 알파벳 수 +1 하고 해당 글자를 문자열에서 삭제
        # print(string)

    elif string[0:2] in ca_lst:
        cnt += 1
        string = string.replace(string[0:2], '', 1)
        # print(string)

    else:
        cnt += 1
        string = string.replace(string[0], '', 1)
        # print(string)

print(cnt)







# for n in range(len(string)):
#     # if string[n] == 'c':
#     #     if string[n+1] == '=' or string[n+1] == '-':
#     #         cnt += 1
#     #         string.replace(string[n:n+2], '')
#     #         # string.replace(string[n+1], '')
#     # if string[n] == 'd':
#     #     if string[n+1] == 'z' and string[n+2] == '=':
#     #         cnt += 1
#     #         string.replace(string[n:n+3], '')
#     #     if string[n+1] == '-':
#     #         cnt += 1
#     #         string.replace(string[n:n+2], '')

#     if string[n:n+3] == 'dz=':
#         cnt += 1
#         string.replace(string[n:n+3], '')

#     elif string[n:n+2] in ca_lst:
#         cnt += 1
#         string.replace(string[n:n+2], '')
    
#     else:
#         cnt += 1
#         string.replace(string[n], '')
    
# print(cnt)
        





    # chr in ca_lst:
    #     # cnt += 1
    #     # string.replace(chr, '')
    # else:
    #     cnt += 1
    #     string.replace(chr, '')