import sys
sys.stdin = open('input.txt')

def bfs(s, N):
    visited = [0] * (N + 1)
    q = []
    q.append(s)
    visited[s] = 1

    while q:
        t = q.pop(0)
        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = 1 + visited[t]

    if visited[G] != 0:
        print(visited[G]-1)
    else:   # 연결 안 되어 있을 경우 visited[G] == 0
        print(0)

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n2].append(n1)
        graph[n1].append(n2)
    S, G = map(int, input().split())

    bfs(S, V)


