import sys
input = sys.stdin.readline

for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if x2 > p1 or y2 > q1 or p2 < x1 or q2 < y1:
        result = 'd'

    elif x1 == p2  or x2 == p1:
        if y2 == q1 or q2 == y1:
            result = 'c'
        else:
            result = 'b'

    elif q1 == y2 or q2 == y1:
        result = 'b'
    else:
        result = 'a'

    print(result)


    # else:
    #     for i in range(x1, p1+1):
    #         if i == x2 or i == p2:
    #             if y2 == q1 or y1 == q2:
    #                 result = 'b'
    #                 break
    #     for j in range(y1, q1+1):
    #         if j == y2 or j == q2:
    #             if x2 == p1 or x1 == p2:
    #                 result = 'b'
    #                 break







    # fw = set(range(x1, p1+1))       # 첫번째 사각형 가로 범위
    # fh = set(range(y1, q1+1))       # 첫번째 사각형 세로 범위
    # sw = set(range(x2, p2+1))       # 두번째 사각형 가로
    # sh = set(range(y2, q2+1))       # 두번째 사각형 세로
    #
    # w = fw & sw                     # 가로 교집합(가로 겹치는 부분)
    # h = fh & sh                     # 세로
    #
    # print([w, h])
    # print(all([w, h]))
    # if not all([w, h]):
    #     result = 'd'
    # else:
    #     if len(w) == 1 and len(h) == 1:
    #         result = 'c'
    #     elif len(w) == 1 or len(h) == 1:
    #         result = 'b'
    #     else:
    #         result = 'a'
    # print(result)
    # elif (len(w) == 1 and len(h) > 1) or (len(h) == 1 and len(w) > 1):
    #     result = 'b'
    # else:
    #     result = 'a'




    # result = 'a'
    # lst1 = [[x1, y1], [x1, q1], [p1, q1], [p1, y1]]
    # lst2 = [[x2, y2], [x2, q2], [p2, q2], [p2, y2]]
    #
    # if (x2 > p1 and y2 > q1) or (p2 < x1 and q2 < y1):
    #     result = 'd'
    #
    # elif x1 == p2 and (y1 == q2 or q1 == y2):
    #     result = 'c'
    # elif x2 == p1 and (y2 == q1 or q2 == y1):
    #     result = 'c'
    #
    # else:
    #     for i in range(x1, p1+1):
    #         if i == x2 or i == p2:
    #             if y2 == q1 or y1 == q2:
    #                 result = 'b'
    #                 break
    #     for j in range(y1, q1+1):
    #         if j == y2 or j == q2:
    #             if x2 == p1 or x1 == p2:
    #                 result = 'b'
    #                 break
    #
    # print(result)



    #
    # if y2 == q1 and (x2 in range(x1, p1) or p2 in range(x1, p1)):   # 위 선분에서 만날 때
    #     result = 'b'
    # if q2 == y1 and (x2 in range(x1, p1) or p2 in range(x1, p1)):   # 아래 선분에서 만날 때
    #     result = 'b'
    # if x2 == p1 and (y2 in range(y1, q1) or q2 in range(y1, q1)):   # 오른쪽
    #     result = 'b'
    # if p2 == x1 and (y2 in range(y1, q1) or q2 in range(y1, q1)):   # 왼쪽
    #     result = 'b'
    #
    # else:
    #     for i in range(4):
    #         if (i < 2 and lst1[i] == lst2[i+2]) or (i >= 2 and lst1[i] == lst2[i-2]):
    #             # lst1이 0, 1일 때 lst2의 2, 3값과 같으면 점 겹침
    #             result = 'c'
    #             break






    #
    # # a인 조건 추가
    # for i in range(p1-x1):
    #     for j in range(q1-y1):
    #         if [x1+i, y1+j] in lst2:
    #             result = 'a'
    #             break

    # print(result)

    # if lst1[i] == lst2[i]:      # 같은 인덱스의 모서리가 같은 경우 사각형으로 겹침
    #     result = 'a'
    #     break














    # if result == 'd':
    #     arr = [[0] * p1 for _ in range(q1)]
    #     for i in range(p1-x1):
    #         for j in range(q1-y1):
    #             arr[x1-i][y1-j] = 1
    #
    #     for a in arr:
    #         print(a)
    #     print()
    #
    #     # for k in range(p2-x2):
    #     #     for l in range(q2-y2):
    #     #         if 0 <= x2-k < p1 and 0 <= y2-l < q1:
    #     #             if arr[x2-k][y2-l] == 1:
    #     #                 result = 'a'
    #     #                 break









    # if lst2[0][1] == q1 and lst2[0][0] in [x1, p1]:     # 두번째 사각형이 첫번째 사각형 위 선분에서 만날 때
    #     result = 'b'
    # if lst2[1][0] == p1 and lst2[1][1] in [y1, q1]:     # 오른쪽 선분에서 만날 때
    #     result = 'b'
    # if lst2[2][1] == y1 and lst2[2][0] in [x1, p1]:     # 아래 선분에서 만날 때
    #     result = 'b'
    # if lst2[3][0] == x1 and lst2[3][0] in [y1, q1]:     # 왼쪽 선분에서 만날 때
    #     result = 'b'

    # print(result)

    # for i in lst1:
    #     if i in lst2:
    #         result = 'c'


    # for i in range(p1-x1):
    #     for j in range(q1-y1):
    #         arr[x1-i][y1-j] = 1
    #
    # for i in range(p2-x2):
    #     for j in range(q2-y2):
    #         arr[x2-i][y2-j] = 2
    #         if arr[x2-i][y2-j] == 1:
    #             result = 'a'
    #             break
    #

