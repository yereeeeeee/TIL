import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = sorted(list(map(int, input().split())))

dp = [False] * 40001
for i in range(1, n+1):
    comb_list = list(combinations(weights, i))
    print(comb_list)
    for comb in comb_list:
        dp[sum(comb)] = True

for i in range(m):
    print('Y' if dp[marbles[i]] else 'N', end=' ')