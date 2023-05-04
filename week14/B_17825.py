import sys
input = sys.stdin.readline

dice_num = list(map(int, input().split()))
# lst = [0] * 41
# 말의 위치 저장하는 딕셔너리?


def sol(dice):
    for i in range(dice+1, 11):
        for num in range(1, 5):
#            만약 해당 말이 주사위 눈 수만큰 이동할 자리에 말이 없으면 이동
            # 네 개 다 해보기

