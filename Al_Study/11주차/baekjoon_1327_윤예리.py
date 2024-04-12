import sys
input = sys.stdin.readline
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(15000)

def bfs():
    visited = set()
    q = deque([])
    q.append([arr, 0])

    while q:
        now_lst, cnt = q.popleft()

        if now_lst == answer:
            return cnt

        for i in range(n-k+1):
            origin =

    else:
        return -1

n, k = map(int, input().split())
arr = list(map(int, input().split()))
answer = sorted(arr)
print(bfs())


