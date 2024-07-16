import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
arr =[int(input()) for _ in range(n)]

notes = [m] * (n+1)
while arr:
    x = arr.pop(0)
    print(arr, notes, x)

    for i in range(n+1):
        if notes[i] < x:
            continue
        else:
            notes[i] -= x
            notes[i] = max(notes[i] - 1, 0)
            break
