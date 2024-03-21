import sys
sys.stdin = open("input.txt")
from heapq import *
import math

def prim(start):
    pq = []
    MST = [0] * n

    sum_weight = 0

    heappush(pq, (0, start))

    while pq:
        weight, now = heappop(pq)

        if MST[now]:
            continue

        MST[now] = 1
        sum_weight += (weight**2)*e

        for to in range(n):
            if graph[now][to] == 0 or MST[to]:
                continue

            heappush(pq, (graph[now][to], to))

    return sum_weight


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())

    graph = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            graph[i][j] = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
            graph[j][i] = math.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)

    # print(graph)
    print(round(prim(0)))