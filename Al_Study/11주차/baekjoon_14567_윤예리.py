import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
idx = [0] * (n+1)   # 진입 차수
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    idx[b] += 1

q = deque([])

for i in range(1, n+1):
    if idx[b] == 0:
        q.append(i)

result = []
while q:
    now = q.popleft()
    result.append(now)

    for next_ in graph[now]:
        idx[next_] -= 1
        if not idx[next_]:
            q.append(next_)
        result
