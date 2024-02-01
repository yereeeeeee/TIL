import sys
sys.stdin = open('input.txt')

for _ in range(10):
    test_case = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착지 좌표 찾기
    end = []
    for i in range(100):
        if 2 in arr[i]:
            end = [i, arr[i].index(2)]

    r = end[0]
    c = end[1]
    #print(r, c)
    while r != 0 and 0 <= c < 100:
        # 현재 위치가 맨 왼쪽일 때
        if c == 0:
            if arr[r][c+1] == 1:
                arr[r][c] = 0
                c += 1
            elif arr[r - 1][c] == 1:
                arr[r][c] = 0
                r -= 1
        # 현재 위치가 맨 오른쪽일 때
        elif c == 99:
            if arr[r][c - 1] == 1:
                arr[r][c] = 0
                c -= 1
            elif arr[r - 1][c] == 1:
                arr[r][c] = 0
                r -= 1
        else:
            if arr[r][c-1] == 1:
                arr[r][c] = 0
                c -= 1
            elif arr[r][c+1] == 1:
                arr[r][c] = 0
                c += 1
            elif arr[r - 1][c] == 1:
                arr[r][c] = 0
                r -= 1
            else:
                break
        # print(r, c)
    print(f'#{test_case} {c}')

