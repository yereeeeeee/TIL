import sys
sys.stdin = open('input.txt')
# from itertools import permutations

def find(x, value):
    global min_v
    if value > min_v:
        return

    if x == N:
        if value < min_v:
            min_v = value
            return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find(x+1, value+arr[x][i])
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 100
    P = [i for i in range(N)]
    visited = [0] * N
    find(0, 0)
    print(min_v)



    # 메모리 초과 ㅠㅠ
    # ls = list(permutations(P, N))   # 순열
    # # print(ls)
    # for i in ls:    # 순열별로 계산
    #     value = 0
    #     for j in range(N):
    #         value += arr[j][i[j]]   # 0번째 행, 0번째 경우, 0, 1, 2 번 숫자를 선택
    #     if min_v > value:
    #         min_v = value
    # print(min_v)