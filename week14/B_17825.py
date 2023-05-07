import sys
input = sys.stdin.readline

# 이동할 위치
rotate = [i for i in range(1, 21)]
rotate += [32, 22, 23, 24, 30, 26, 24, 28, 29, 24, 31, 20, 32]

game = []  # 게임판 점수
for s in range(0, 41, 2):
    game.append(s)
game += [13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]

dice = list(map(int, input().split()))
horse = [0, 0, 0, 0]  # 말 위치 저장
turn = {5: 21, 10: 25, 15: 27}  # 파란색 칸일 경우 방향 바꾸기(key값에서 value의 인덱스로 이동)
result = 0

def sol(idx, score):
    global result
    if idx >= 10:  # 주사위 10개 다 씀
        result = max(result, score)
        return

    for i in range(4):
        h = horse[i]
        if h in turn:     # 파란색 칸이면 방향 바꿔서 갈 인덱스로
            h = turn[h]
        else:
            h = rotate[h]   # 아니면 rotate에 저장된 값

        for j in range(1, dice[idx]):
            h = rotate[h]   # 해당 주사위 눈 수만큼 이동

        # 도착했거나 말이 겹치지 않아 이동가능하다면
        if h == 32 or (h < 32 and h not in horse):
            tmp = horse[i]
            horse[i] = h
            sol(idx + 1, score + game[h])
            horse[i] = tmp

sol(0, 0)
print(result)


##################
# dice = list(map(int, input().split()))
# game = []  # 게임판 점수
# for s in range(0, 41, 2):
#     game.append(s)
# game += [13, 16, 19, 25, 22, 24, 28, 27, 26, 30, 35, 0]
#
# # 이동할 인덱스
# rotate = [i for i in range(1, 21)]
# rotate += [32, 22, 23, 24, 30, 26, 24, 28, 29, 24, 31, 20, 32]
#
# horse = [0, 0, 0, 0] # 말 위치 기록
# turn = {5: 21, 10: 25, 15: 27}  # 파란색 칸일 경우 방향 바꾸기(key값에서 value의 인덱스로 이동)
# result = 0
#
#
# def sol(idx, score):
#     global result
#     if idx == 10:
#         result = max(result, score)
#         return
#
#     for n in range(4):
#         h = horse[n]
#         if h in turn:     # 파란색 칸이면 방향 바꿔서 갈 인덱스로
#             h = turn[h]
#         else:
#             h = rotate[h] # 아니면 rotate에 저장된 값
#         for i in range(1, dice[idx]):   # 해당 주사위 눈 수만큼 이동
#             h = rotate[h]
#
#         # 도착했거나 말이 겹치지 않아 이동가능하다면
#         if h == 32 or (h < 32 and h not in horse):
#             tmp = horse[n]
#             horse[n] = h
#             sol(idx+1, score+game[n])
#             horse[n] = tmp
#
# sol(0, 0)
# print(result)
#
#
#
#    # 만약 해당 말이 주사위 눈 수만큰 이동할 자리에 말이 없으면 이동
#    #  네 개 다 해보기
#
#
#
#
# # game.append([i for i in range(0, 41, 2)])
# # game.append([10, 13, 16, 19, 25, 30, 35, 40])
# # game.append([20, 22, 24, 25, 30, 35, 40])
# # game.append([30, 28, 27, 26, 25, 30, 35, 40])

# tmp = horse[n]
# horse[n] += dice[n]
# sol(idx + 1, score + game[n])
# horse[n] -= dice[n]


###################