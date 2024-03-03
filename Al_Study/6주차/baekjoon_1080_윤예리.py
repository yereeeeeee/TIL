n, m = map(int, input().split())
if n < 3 or m < 3:
    exit(print(-1))

A = [list(map(int, input())) for _ in range(n)]
B = [list(map(int, input())) for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):
        