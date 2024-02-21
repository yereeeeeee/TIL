import sys
sys.stdin = open('input.txt')

n = int(input())
par = [0] * (n+1)
chd = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c = map(int, input().split())
    if
for i in range(2, n+1):
    print(par[i])