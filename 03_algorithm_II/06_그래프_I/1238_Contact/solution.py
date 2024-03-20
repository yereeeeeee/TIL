import sys
sys.stdin = open("input.txt")
from collections import deque

def bfs(v):
    q = deque([v])
    visited[v] = 1

    while q:
        t = q.popleft()

        for i in graph[t]:
            if visited[i] == 0:
                q.append(i)
                visited[i] = visited[t]+1


for tc in range(1, 11):
    n, start = map(int, input().split())
    graph = [[] for _ in range(101)]
    data = list(map(int, input().split()))
    visited = [0] * 101
    for i in range(n):
        if not i%2:
            graph[data[i]].append(data[i+1])

    bfs(start)

    result = 0
    for j in range(len(visited)):
        if visited[j] == max(visited):
            if j > result:
                result = j
    print(f'#{tc} {result}')