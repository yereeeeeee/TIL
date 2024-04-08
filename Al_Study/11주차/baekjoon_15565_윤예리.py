import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 라이언이 k개가 안 될 때
if arr.count(1) < k:
    exit(print(-1))

