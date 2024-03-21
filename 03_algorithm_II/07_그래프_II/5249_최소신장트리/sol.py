import sys
sys.stdin = open('input.txt')
from heapq import *

# KRUSKAL algorithm
def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    v, e = map(int, input().split())
    edges = []

    for _ in range(e):
        s, e, w = map(int, input().split())
        edges.append([s, e, w])
    edges.sort(key=lambda x:x[2])
    parents = [i for i in range(v+1)]

    cnt = 0
    sum_weight = 0

    for s, e, w in edges:
        if find_set(s) == find_set(e):
            continue

        cnt += 1
        union(s, e)
        sum_weight += w

        if cnt == v:
            break

    print(sum_weight)

# prim algorithm
# def prim(start):
#     pq = []
#     MST = [0] * v
#
#     sum_weight = 0
#     heappush(pq, (0, start))
#
#     while pq:
#         weight, now = heappop(pq)
#
#         if MST[now]:
#             continue
#
#         MST[now] = 1
#         sum_weight += weight
#
#         for to in range(v):
#             if graph[now][to] == 0 or MST[to]:
#                 continue
#
#             heappush(pq, (graph[now][to], to))
#
#     return sum_weight
#
#
# T = int(input())
# for tc in range(1, T+1):
#     print(f'#{tc}', end=' ')
#     v, e = map(int, input().split())
#     graph = [[0] * (v+1) for _ in range(v+1)]
#
#     for _ in range(e):
#         n1, n2, w = map(int, input().split())
#         graph[n1][n2] = w
#         graph[n2][n1] = w
#
#     print(prim(0))