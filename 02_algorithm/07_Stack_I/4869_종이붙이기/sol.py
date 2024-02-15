import sys
sys.stdin = open('input.txt')

memo = [0] * 31
memo[1] = 1
memo[2] = 3
for i in range(3, len(memo)):
    for j in range(1, i):
        memo[i] += memo[j]
    memo[i] += 1
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    n = N // 10
    print(memo[n])

