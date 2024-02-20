import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    N = int(input())

    # idx
    left_idx = [0] * (N+1)
    right_idx = [0] * (N+1)
    par_idx = [0] * (N+1)
    node_idx = [0] * (N+1)

    numbers = []
    for i in range(2, N+1):
        numbers.append(i)

    i = 1
    while numbers:
        if left_idx[i] == 0:
            left_idx[i] = numbers.pop(0)
            par_idx[left_idx[i]] = i
        if not numbers:
            break
        if right_idx[i] == 0:
            right_idx[i] = numbers.pop(0)
            par_idx[right_idx[i]] = i
        i += 1

    # 시작점 찾기
    start = 1
    while left_idx[start] != 0:
        start = left_idx[start]
    #print(start)

    value = []
    def in_order(T):
        if T:
            in_order(left_idx[T])
            value.append(T)
            in_order(right_idx[T])
    in_order(1)

    print(value.index(1)+1, value.index(N//2)+1)



