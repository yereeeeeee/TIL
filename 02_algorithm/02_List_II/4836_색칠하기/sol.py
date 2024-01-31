import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    red = []
    blue = []
    for n in range(N):
        square = list(map(int, input().split()))
        if square.pop() == 1:
            red.append(square)
        else:
            blue.append(square)

    # 빨간 사각형
    red_area = []
    for R in range(len(red)):
        for x1 in range(red[R][0], red[R][2] + 1):
            for y1 in range(red[R][1], red[R][3] + 1):
                red_area.append([x1, y1])

    # 파란 사각형
    blue_area = []
    for B in range(len(blue)):
        for x2 in range(blue[B][0], blue[B][2] + 1):
            for y2 in range(blue[B][1], blue[B][3] + 1):
                blue_area.append([x2, y2])

    count = 0
    for purple in red_area:
        if purple in blue_area:
            count += 1
    print(f'#{test_case} {count}')