import sys
sys.stdin = open('input.txt')

import heapq
t = int(input())
for tc in range(1, t+1):
    h = []

    K = int(input())
    for k in range(K):
        char, N = map(str, input().split())
        n = int(N)

        if char == 'I':
            heapq.heappush(h, n)

        if char == 'D':
            if n == 1:
                if h:
                    h.pop(0)
            else:
                if h:
                    heapq.heappop(h)
    if h:
        print(h)
        print(max(h), min(h))
    else:
        print('EMPTY')
