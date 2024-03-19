import sys
sys.stdin = open('input.txt')

def backtraking(i, per):
    global result

    if per <= result:
        return

    if i == n:
        if per > result:
            result = per
            return

    for j in range(n):
        if not visited[j]:
            visited[j] = 1
            backtraking(i+1, per*(p[i][j]/100))
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    lst = []
    print(f'#{tc}', end=' ')
    n = int(input())
    p = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    visited = [0] * n
    backtraking(0, 1)

    print('%.6f'%(result*100))

# 메모리 초과
# from itertools import permutations
# T = int(input())
# for tc in range(1, T+1):
#     print(f'#{tc}', end=' ')
#     n = int(input())
#     p = [list(map(int, input().split())) for _ in range(n)]
#     num_list = [i for i in range(n)]
#     per_ = list(permutations(num_list, n))
#     result = 0
#
#     for j in range(len(per_)):
#         tmp = 1
#         for i in range(n):
#             tmp *= p[i][per_[j][i]] / 100
#
#         if tmp * 100 > result:
#             result = tmp * 100
#
#     print('%.6f'%result)


