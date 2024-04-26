import sys
input = sys.stdin.readline

n, m = map(int, input().split())
per_n = sorted(list(map(int, input().split())))
per_m = sorted(list(map(int, input().split())))

for i in range(min(n, m)):
    