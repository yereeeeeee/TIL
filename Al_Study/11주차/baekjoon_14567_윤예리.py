import sys
input = sys.stdin.readline
from collections import deque

def find(x):
    if par[x]:
        for y in par[x]:
            if y not in graph[i]:
                graph[i].append(y)
            find(y)

n, m = map(int, input().split())
par = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    par[b].append(a)    # b의 부모는 a

graph = [[] for _ in range(n+1)]
for i in range(1, n+1):
    find(i)
print(graph)
