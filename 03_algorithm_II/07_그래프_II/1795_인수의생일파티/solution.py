import sys
sys.stdin = open("input.txt")
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

    n, m, X = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        x, y, c = map(int, input().split())
        graph[x].append((c, y))

    tmp = [[]]
    for i in range(n):
        distance = [float('inf')] * (n+1)
        tmp.append(dijkstra(i+1))

    result = 0
    for j in range(1, n+1):
        if tmp[j][X] + tmp[X][j] > result:
            result = tmp[j][X] + tmp[X][j]
    print(result)

