import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    ls = list(map(int, input().split()))
    print(f'#{tc} {ls[m%n]}')