import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split()))
    ls = []
    result = 0

    print(f'#{tc}', end=' ')
    for i in cost:
        max_value = max(cost)
        for j in range(cost.index(max_value)+1):
            if cost[j] == max_value:
                result += len(ls) * cost[j] - sum(ls)
                for k in range(cost.index(max_value)+1):
                    cost.pop(0)
                ls = []
            else:
                ls.append(cost[j])

    if result > 0:
        print(result)
    else:
        print(0)