N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# 2차원 배열 부분합 누적합
S = 

# 시간 초과
# for m in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     total = 0
#     for i in range(x1-1, x2):
#         for j in range(y1-1, y2):
#             total += arr[i][j]
#     print(total)
