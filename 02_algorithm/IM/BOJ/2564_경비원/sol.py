import sys
sys.stdin = open('input.txt')

n, m = map(int, input().split())    # 블록의 가로, 세로 길이
k = int(input())    # 상점의 개수
for _ in range(k):
