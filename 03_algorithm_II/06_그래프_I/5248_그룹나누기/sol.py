import sys
sys.stdin = open('input.txt')

def dfs(i, arr):
    visited[i] = 1

    for j in arr:
        if not visited[j]:
            dfs(j, graph[j])

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n, m = map(int, input().split())
    visited = [0] * (n+1)

    # 그래프 만들기
    graph = [[] for _ in range(n+1)]
    a = list(map(int, input().split()))
    for b in range(m*2):
        if not b % 2:
            graph[a[b]].append(a[b+1])
            graph[a[b+1]].append(a[b])

    cnt = 0
    k = 1
    while sum(visited) < n:
        if not visited[k]:
            dfs(k, graph[k])
            cnt += 1
        k += 1

    print(cnt)