import sys
sys.stdin = open('input.txt')
import heapq

def dijkstra(graph, start):
    weight = {node: float('inf') for node in graph}
    weight[start] = 0
    q = []
    heapq.heappush(q, [weight[start], start])

v, e = map(int, input().split())
k = int(input())
graph = {}
for i in range(v):
    graph[i] =
for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append({v:w})
print(graph)