import sys
sys.stdin = open('input.txt')
from heapq import *

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dijkstra(start):
    pq = [(0, start)]
    distance[start] = 0

    while pq:
        dist, now = heappop(pq)

        if distance[now] < dist:


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n = int(input())
    start = 0
    graph = [list(map(int, input().split())) for _ in range(n)]

    distance = [float('inf')] * n

