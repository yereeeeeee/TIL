import sys
input = sys.stdin.readline

# 크루스칼
v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
