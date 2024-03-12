n = int(input())
child = [[] for _ in range(n+1)]
par = []
for _ in range(n-1):
    a, b = map(int, input().split())

# 방향 없는 트리
