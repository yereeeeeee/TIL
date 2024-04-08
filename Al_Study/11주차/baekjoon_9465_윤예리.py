# DP
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    n = int(input())
    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))
    tmp = 0
    print(arr)