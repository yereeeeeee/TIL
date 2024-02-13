import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    stack = []
    top = -1
    # visited = [[0] * N for _ in range(N)]

    # 출발지 찾기 (st[0])
    while top == -1:
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 2:
                    stack.append([i, j])
                    top += 1
    x = stack[top][0]
    y = stack[top][1]

    # 탐색
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    while 1:
        for i in range(4):
            if 0 <= x + dx[i] < N and 0 <= y + dx[i] < N:
                # 4 방향에 0이 있으면
                if arr[x + dx[i]][y + dy[i]] == 0:
                    x = x + dx[i]   # 이동
                    y = y + dy[i]
                    arr[x][y] = 1   # 새로 온 위치를 1로 바꾸고
                    stack.append([x, y])    # stack에 push
                    top += 1
                # 3이 있으면
                elif arr[x + dx[i]][y + dy[i]] == 3:
                    print(1)        # print하고 종료
                    break
            break
        else:
            point = stack.pop(top)
            top -= 1
            x = point[0]
            y = point[1]
