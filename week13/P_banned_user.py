def solution(user_id, banned_id):
    answer = 0
    result = []
    used = [0] * len(user_id)

    def check(b_idx, tmp, cnt):
        # 불량 사용자 목록의 수 == cnt가 되면 tmp복사본을 result에 추가 후 return
        if cnt == len(banned_id):
            ans = list(tmp)
            result.append(ans)
            return

        for u in range(len(user_id)):
            flag = True
            if len(banned_id[b_idx]) != len(user_id[u]):    # 길이 다르면 가망 없음 -> continue
                flag = False
                continue
            for b in range(len(banned_id[b_idx])):
                if banned_id[b_idx][b] == '*':    # 불량 사용자 아이디 중 *인 자리는 확인 필요 없음
                    continue
                if banned_id[b_idx][b] != user_id[u][b]:  # 글자 다르면 가망 없음 -> flag 바꾸고 for문 벗어나기
                    flag = False
                    break
            if flag:                # 모든 조건 통과 -> 해당 불량 사용자 가능
                if not used[u]:     # 사용한 적 없을 때만 체크
                    used[u] = 1
                    tmp[b_idx] = user_id[u]         # tmp의 b_idx 위치에 가능성 있는 user id 넣기
                    check(b_idx + 1, tmp, cnt+1)    # cnt + 1하고, 그 다음 불량 사용자 체크
                    used[u] = 0                     # 리턴해서 돌아오면 초기화
                    tmp[b_idx] = ""

    tmp = ["" for _ in range(len(banned_id))]
    check(0, tmp, 0)

    answer_lst = []
    for r in range(len(result)):
        result[r].sort()
        if result[r] not in answer_lst:     # 정렬 후 not in으로 중복값 없애기
            answer_lst.append(result[r])

    answer = len(answer_lst)
    return answer





user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "abc1**"]
# banned_id = ["*rodo", "*rodo", "******"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))






# result = []
# print(solution(user_id, banned_id))
# print(result)

#
# def solution(user_id, banned_id):
#     answer = 0
#     # tmp = ["" for _ in range(len(banned_id))]
#     result = []
#     tmp = []
#
#     def check(user, ban):
#         if len(user) != len(ban):
#             return False
#
#         for b in range(len(ban)):
#             if ban[b] == '*':
#                 continue
#             if user[b] != ban[b]:
#                 return False
#         return True
#
#     for i in user_id:
#         for j in banned_id:
#             flag = check(i, j)
#             if flag:
#                 if i not in tmp:
#                     tmp.append(i)
#             # print('user, ban: ', user_id[i], banned_id[j])
#             # print(flag)
#             # print()
#
#
#     # for i in user_id:
#     #     for j in banned_id:
#     #         flag = check(i, j)
#     #         if flag:
#     #             if i not in tmp:
#     #                 tmp.append(i)
#
#     print(tmp)
#     return answer
#
# solution(user_id, banned_id)












#     for i in user_id:
#         flag = True
#         if len(i) != len(banned_id[idx]):
#             continue
#         for b in range(len(banned_id[idx])):
#             if banned_id[idx][b] == '*':
#                 continue
#             if banned_id[idx][b] != i[b]:
#                 flag = False
#                 break
#         if flag:
#             tmp[idx].append(i)
