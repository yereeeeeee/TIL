def backtrack(x):
    if len(stack) == m:
        print(*stack)
        return

    if len(stack) > m:
        return

    for i in range(n):
        if arr[i] not in stack:
            stack.append(arr[i])
            backtrack(x+1)
            stack.pop()


n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
visited = [0] * n
stack = []
backtrack(0)