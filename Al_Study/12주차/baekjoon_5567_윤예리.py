import sys
input = sys.stdin.readline

def find(x):
    pass

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b].append(a)

print(graph)