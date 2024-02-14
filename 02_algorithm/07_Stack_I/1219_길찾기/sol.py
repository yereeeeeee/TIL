import sys
sys.stdin = open('input.txt')

def dfs(start):
    visited[start] = 1
    stack = [start]

    while stack:
        now = stack.pop()
        visited[now] = 1
        for next in adjl[now]:
            if not visited[next]:
                stack.append(next)

for _ in range(10):
    tc, length = map(int, input().split())
    num_set = list(map(int, input().split()))

    adjl = [[] for _ in range(100)]
    visited = [0] * 100

    for i in range(length):
        adjl[num_set[i*2]].append(num_set[i*2+1])

    dfs(0)
    print(f'#{tc} {visited[99]}')