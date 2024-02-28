import sys
sys.stdin = open('input.txt')

'''
1. 먼저 끝나고
2. 먼저 시작하는 애들
순으로 정렬해서 고려하면 편함
'''

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n = int(input())
    ls = []
    for _ in range(n):
        s, e = map(int, input().split())
        ls.append((s, e))
    ls.sort(key=lambda x : (x[1], x[0]))

    cnt = 1
    stack = [ls[0]]
    for i in range(1, n):
        start = ls[i][0]    # 다음 작업 시작 시간
        end = stack[-1][1]    # 이전 작업 종료 시간

        if start >= end:
            cnt += 1
            stack.append(ls[i])

    print(cnt)