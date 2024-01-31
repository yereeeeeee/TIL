import sys
sys.stdin = open('input.txt')

A = []
for a in range(1, 13):
    A.append(a)

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())

    for n in range(N):
        arr = [0] * N
        i = 0
        while i < 13:

