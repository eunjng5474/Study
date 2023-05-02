def solution(n, build_frame):
    answer = []

    # answer 내의 모든 값에 대해 확인해서 패스해야 True!
    def check(answer):
        for x, y, num in answer:
            if num:   # 보
                if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                    continue
                return False  # 조건 미충족 시 return False로 종료

            else:   # 기둥
                if y == 0 or [x, y, 1] in answer or [x-1, y, 1] in answer or [x, y-1, 0] in answer:
                    continue
                return False
        return True  # 모든 for문을 return False 없이 통과해야 True


    for x, y, a, b in build_frame:
        # 설치/삭제 후 문제 없는지 확인
        # 문제 있다면 다시 삭제하거나 추가하여 해당 작업 무시
        if b:
            answer.append([x, y, a])
            if not check(answer):
                answer.remove([x, y, a])
        else:
            answer.remove([x, y, a])
            if not check(answer):
                answer.append([x, y, a])

    answer.sort()
    return answer


n = 5
# build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))







##########
# def solution(n, build_frame):
#     answer = []
#     arr = [[2] * (n+1) for _ in range(n+1)] # 0이 기둥이니까 초기값 2
#
#     ##### check(x, y, num)으로 해당 좌표에 num 들어가도 되는지 확인하는 함수 만들기
#     def check(x, y, num):
#         if num:
#             if arr[x+1][y] == 0 or arr[x+1][y+1] == 0 or (arr[x][y-1] == 1 and arr[x][y+1] == 1 and arr[x][y] == 1):
#                 return True
#                 # arr[x][y] = b[2]
#         else:
#             if x == n or arr[x + 1][y] == 0 or arr[x][y] == 1 or arr[x][y - 1] == 1:
#                 # arr[x][y] = b[2]
#                 return True
#         return False
#
#
#     for b in build_frame:
#         x, y = n - b[1], b[0]
#         if b[3]:
#             arr[x][y] = b[2]
#             # x, y, num = n - b[1], b[0], b[2]
#             if not check(x, y, b[2]):
#                 arr[x][y] = 2
#         else:
#             # x, y, num = n - b[1], b[0], 2
#             arr[x][y] = 2
#             if not check(x, y, b[2]):
#                 arr[x][y] = b[2]
#
#     for a in arr:
#         print(a)
#     print()
#
#     for i in range(n+1):
#         for j in range(n+1):
#             if arr[i][j] != 2:
#                 answer.append([j, n-i, arr[i][j]])
#
#     answer.sort()
#     return answer