import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'# {tc}')
    N = int(input())

    def p_tri(n):
        if n == 0:
            return [1]
        elif n == 1:
            return [1, 1]
        else:
            mid = []
            for i in range(n-1):
                mid.append(p_tri(n-1)[i] + p_tri(n-1)[i+1])
            return [1, *mid, 1]

    for j in range(N):
        print(*p_tri(j))


# 메모리 에러
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#
#     def p_tri(n):
#         global memo
#         if n >= 2:
#             result = []
#             a = []
#             for i in range(n-1):
#                 a.append(memo[n-1][i]+memo[n-1][i+1])
#             result.append(1)
#             result.extend(a)
#             result.append(1)
#             memo[n] = result
#             return memo[n]
#
#     memo = [0] * (N)
#     memo[0] = [1]
#     memo[1] = [1, 1]
#
#     print(f'#{tc}')
#     for i in range(N):
#         p_tri(i)
#         print(*memo[i])
