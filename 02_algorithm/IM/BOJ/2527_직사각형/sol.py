import sys
sys.stdin = open('input.txt')

for _ in range(4):
    ls = list(map(int, input().split()))

    # 첫 번째 직사각형
    s1 = ls[:4]
    x1 = [i for i in range(s1[0], s1[2]+1)]
    y1 = [i for i in range(s1[1], s1[3]+1)]

    # 두 번째 직사각형
    s2 = ls[4:]
    x2 = [i for i in range(s2[0], s2[2]+1)]
    y2 = [i for i in range(s2[1], s2[3]+1)]

    intersection_x = list(set(x1) & set(x2))
    intersection_y = list(set(y1) & set(y2))

    if len(intersection_x) > 1 and len(intersection_y) > 1: # 겹치는 부분이 직사각형
        print('a')
    elif len(intersection_x) == 0 and len(intersection_y) == 0: # 겹치는 부분이 아예 없을 때
        print('d')
    elif len(intersection_x) == 1 and len(intersection_y) == 1: # 점으로 겹칠 때
        print('c')
    else:
        print('b')