string = input()
cnt = 0
ca_lst = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

while string:
    if string[0:3] == 'dz=':
        cnt += 1
        string = string.replace(string[0:3], '', 1)
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