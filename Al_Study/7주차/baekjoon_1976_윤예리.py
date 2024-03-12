n, m = int(input()), int(input())
graph = [[] for _ in range(n+1)]

trip = map(int, input().split())
for i in range(m):
