import sys
sys.stdin = open('input.txt')
'''
1. 1일 이용권
2. 1달 이용권(매달 1일부터 시작)
3. 3달 이용권(연속된 3달, 다음해로 이월 x)
4. 1년 이용권
'''
def backtracking(i, c):
    global result

    if c >= result:
        return

    if i == 12:
        result = c
        return

    else:
        backtracking(i+1, c+cost[0]*plan[i])  # 1일 이용권
        backtracking(i+1, c+cost[1])    # 1달 이용권
        if i < 10:
            backtracking(i+3, c+cost[2])    # 3달 이용권
        elif i == 10:
            backtracking(i+2, c+cost[2])
        else:
            backtracking(i+1, c + cost[2])


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    cost = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    ls = [0, 1, 2]
    result = float('inf')

    a = 0
    while plan[a] == 0:
        a += 1
    backtracking(a, 0)

    result = min(result, cost[3])
    print(result)