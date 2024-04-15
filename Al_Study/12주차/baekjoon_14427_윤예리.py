# 세그먼트 트리
import sys
input = sys.stdin.readline
from heapq import *

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    b = list(map(int, input().split()))

    if b[0] == 1:
        arr[b[1]-1] = b[2]
    else:
        
        print(arr.index(min(arr))+1)