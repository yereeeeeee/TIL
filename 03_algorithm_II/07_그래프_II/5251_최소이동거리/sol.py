import sys
sys.stdin = open('input.txt')
from heapq import *

def dijkstra(start):
    pq = []
    heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:
            continue

        for to in graph[now]:
            next_dist = to[0]
            next_node = to[1]

            new_dist = dist + next_dist

            if new_dist >= distance[next_node]:
                continue

            distance[next_node] = new_dist
            heappush(pq, (new_dist, next_node))

    return distance


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    v, e = map(int, input().split())
    start = 0

    graph = [[] for _ in range(v+1)]
    distance = [float('inf')] * (v+1)

    for _ in range(e):
        s, e, w = map(int, input().split())
        graph[s].append((w, e))

    print(dijkstra(0)[-1])