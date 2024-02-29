import sys
sys.stdin = open('input.txt')

c, r = map(int, input().split())    # 종이 가로, 세로
n = int(input())    # 점선 개수
hor = []
ver = []
for _ in range(n):
    # 0: 가로, 1: 세로
    dir_, num = map(int, input().split())
    if dir_ == 0:
        hor.append(num)
    else:
        ver.append(num)
