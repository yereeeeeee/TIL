import sys
sys.stdin = open('input.txt')

def dfs(st, V, s):
    V[s] = 1
    for k in graph[s]:
        if V[k] == 0:
            dfs(st, V, k)

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    v, e = map(int, input().split())
    visited = [0] * 51
    stack = []

    graph = [[] for _ in range(51)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    S, G = map(int, input().split())
    dfs(stack, visited, S)
    print(visited[G])