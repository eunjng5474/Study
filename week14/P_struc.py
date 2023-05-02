def solution(n, build_frame):
    answer = [[]]
    arr = [[2] * (n+1) for _ in range(n+1)] # 0이 기둥이니까 초기값 2

    ##### check(x, y, num)으로 해당 좌표에 num 들어가도 되는지 확인하는 함수 만들기
    def check(x, y, num):
        if b[2]:
            if arr[x + 1][y] == 0 or arr[x + 1][y + 1] == 0 or arr[x + 1][y - 1] == 0 or (
                    arr[x][y - 1] == 1 and arr[x][y + 1] == 1):
                return True
                # arr[x][y] = b[2]
        else:
            if x == n or arr[x + 1][y] == 0 or arr[x][y] == 1 or arr[x][y - 1] == 1:
                # arr[x][y] = b[2]
                return True
        return False


    #### 열 + / - 잘 확인하기
    for b in build_frame:
        x, y, num = n - b[1], b[0], b[2]
        # 삭제면 0이어야 함
        if check(x, y, num):




    #     if b[3]:
    #         if b[2]:
    #             if arr[x+1][y] == 0 or arr[x+1][y+1] == 0 or arr[x+1][y-1] == 0 or (arr[x][y-1] == 1 and arr[x][y+1] == 1):
    #                 arr[x][y] = b[2]
    #         else:
    #             if x == n or arr[x+1][y] == 0 or arr[x][y] == 1 or arr[x][y-1] == 1:
    #                 arr[x][y] = b[2]
    #     else:
    #         if



    for a in arr:
        print(a)
    print()


            # if b[3]:
            #     arr[b[0]][b[1]] = b[2]
            # else:
            #     arr[b[0]][b[1]] = 2


    return answer


n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
# build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

solution(n, build_frame)