def cnt(i):

    if len(stack) == m:
        print(*stack)
        return

    for j in range(n):
        if ls[j] not in stack:
            stack.append(ls[j])
            cnt(j)
            stack.pop(0)

n, m = map(int, input().split())
ls = [i for i in range(1, n+1)]
stack = []