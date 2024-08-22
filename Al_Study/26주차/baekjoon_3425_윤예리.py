import sys
input = sys.stdin.readline
from collections import deque

stack = deque([])

while 1:
    comm = input().strip()

    if comm == 'QUIT': break

    if comm[:3] == 'NUM': stack.append(int(comm[3:]))
    if comm == 'POP': stack.pop()
    if comm == 'INV':