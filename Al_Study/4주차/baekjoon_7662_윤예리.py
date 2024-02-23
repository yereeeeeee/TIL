'''
1. 삽입할 때 최소힙으로 만들고
2. 삭제할 때 가장 앞/뒤 요소를 삭제
'''
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

        if char == 'I': # 삽입
            heapq.heappush(h, n)

        if char == 'D':
            if n == 1:  # 최대값 삭제
                if h:   # Q가 비었으면 패스
                    h.pop()
            else:
                if h:   # 최소값 삭제
                    heapq.heappop(h)
    if h:
        #print(h)
        print(h[-1], h[0])
    else:
        print('EMPTY')
