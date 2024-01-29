import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N = int(input())
    a_j = list(map(int, input().split()))
    print(f'#{t+1} {max(a_j) - min(a_j)}')