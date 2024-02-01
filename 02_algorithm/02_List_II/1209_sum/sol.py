# 2차원 리스트 접근법 알아볼 때 좋음
import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    max_value = 0
    for i in range(100):            # 각 행의 합
        value = 0
        for j in range(100):
            value += arr[i][j]
        if max_value < value:
            max_value = value

    for j in range(100):            # 각 열의 합
        value = 0
        for i in range(100):
            value += arr[i][j]
        if max_value < value:
            max_value = value

    v = 0
    for k in range(100):            # 오른쪽 아래로 향하는 대각선의 합
        v += arr[k][k]
    if max_value < v:
        max_value = v

    v = 0
    for k in range(99, -1, -1):            # 왼쪽 아래로 향하는 대각선의 합
        v += arr[k][k]
    if max_value < v:
        max_value = v

    # for i in range(100):                  # 왼쪽 아래로 향하는 대각선의 합 (2)
    #     v += arr[i][100-i]
    # if max_value < v:
    #     max_value = v


    print(f'#{test_case} {max_value}')