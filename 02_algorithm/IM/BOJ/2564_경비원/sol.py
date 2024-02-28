import sys
sys.stdin = open('input.txt')

def clockwise(st, i, j, cnt=0):
    if i == 0:      # 북
        if st in arr[0][j:]:
            cnt += arr[0].index(st)
            return
        else:
            cnt += m-j
            j += m-j

    elif i == n:    # 남
        if st in arr[0][:j]:
            cnt += arr[0].index(st)
            return
        else:
            cnt += j
            j += j




def anti(st, i, j):





m, n = map(int, input().split())    # 블록의 가로(m), 세로 길이(n)
                                    # [10, 6]
arr = [[0] * (m+1) for _ in range(n+1)]
k = int(input())    # 상점의 개수
store = []
for s in range(1, k+1):
    # 1: 북, 2: 남, 3: 서, 4: 동
    # 북, 남: 왼쪽으로부터의 거리
    # 동, 서: 위쪽으로부터의 거리
    direction, distance = map(int, input().split())
    if direction == 1:
        arr[0][distance] = s
    elif direction == 2:
        arr[n][distance] = s
    elif direction == 3:
        arr[distance][0] = s
    else:
        arr[distance][m] = s

    store.append((direction, distance))

d, g = map(int, input().split())
result = 0
for i in range(1, k+1):
    result += min(clockwise(i, d, g), anti(i, d, g))
