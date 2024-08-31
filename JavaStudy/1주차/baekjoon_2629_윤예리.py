import sys
input = sys.stdin.readline

n = int(input())
weights = list(map(int, input().split()))
m = int(input())
marbles = list(map(int, input().split()))

dp = [False] * 15001

def solution(x, idx):
    if dp[x]: return

    dp[x] = True
    # 1. 추만 두는 경우
    if idx == n-1: return
    solution(x+weights[idx+1], idx+1)
    # 2. 추와 구슬을 같이 두는 경우
    solution(abs(x-weights[idx+1]), idx+1)
    

for w in range(n):
    solution(weights[w], w)

for marble in marbles:
    # print(marble, dp[marble])
    if marble > 15000: print('N', end=' ')
    else: print('Y' if dp[marble] else 'N', end=' ')
