import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    E, N = map(int, input().split())
    n = E+1     # 노드 개수

    # 그래프 그리기
    left = [0] * (n+1)
    right = [0] * (n+1)
    par = [0] * (n+1)

    ls = list(map(int, input().split()))
    for i in range(E):
        p, c = ls[i*2], ls[i*2+1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        par[c] = p

    # 노드 개수 찾기
    cnt = 0
    def pre(T):
        global cnt
        if T:
            cnt += 1
            pre(left[T])
            pre(right[T])

    pre(N)
    print(cnt)


