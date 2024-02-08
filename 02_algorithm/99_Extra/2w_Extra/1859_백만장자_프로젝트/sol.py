import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))
    result = 0

    while cost:
        max_value = max(cost)
        max_index = cost.index(max(cost))

        result += (max_index+1) * max_value - sum(cost[:max_index+1])
        del cost[:max_index+1]

    print(f'#{tc} {result}')



    # 시간 초과
    # ls = []
    # result = 0
    # i = 0
    #
    # print(f'#{tc}', end=' ')
    # while i < len(cost):
    #     max_value = max(cost)
    #     for j in range(cost.index(max_value)+1):
    #         if cost[j] == max_value:
    #             result += len(ls) * cost[j] - sum(ls)
    #             for k in range(cost.index(max_value)+1):
    #                 cost.pop(0)
    #             ls = []
    #             i = 0
    #         else:
    #             ls.append(cost[j])
    #             i += 1
    #
    # if result > 0:
    #     print(result)
    # else:
    #     print(0)