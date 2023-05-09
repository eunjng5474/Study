N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
paper = [[0] * M for _ in range(N)]

# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1 and not paper[i][j]:
#             p, q = i, j
#             while q < M:
#                 if not arr[p][q]:
#                     break
#                 paper[p][q] += 1
#                 q += 1
#             cnt += 1
#         if arr[i][j] == 2 and paper[i][j] != 2:
#             p, q = i, j
#             while q < M:
#                 if arr[p][q] != 2:
#                     break
#                 paper[p][q] += 1
#                 q += 1
#             cnt += 1
# print(cnt)
