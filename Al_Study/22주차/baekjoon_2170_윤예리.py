# from collections import deque
from heapq import *

import sys
input = sys.stdin.readline

n = int(input())

hq = []
for _ in range(n):
    x, y = map(int, input().split())
    heappush(hq, (x, y))

start, end = heappop(hq)
result = 0
while hq:
    print(hq)
    new_start, new_end = heappop(hq)

    if start < new_start and end <= new_end:
        end = new_end
    elif new_start > end:
        result += end-start
        start = new_start
        end = new_end
    else:
        print(start, end)

print(result)