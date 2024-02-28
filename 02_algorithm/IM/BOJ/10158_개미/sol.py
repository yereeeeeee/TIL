# import sys
# sys.stdin = open('input.txt')

def move_():
    pass

# 행: h, 열: w
w, h = map(int, input().split())
# arr = [[0] * w for _ in range(h)]

p, q = map(int, input().split())
# 처음 개미 위치: x, y
y = p
x = h-q

t = int(input())
for i in range(t):
    if x == h:      # 오른쪽에 부딪치면
        x -= 1
        y -= 1
    elif y == 0:    # 위에 부딪치면
