import sys
sys.stdin = open('input.txt')

code = [
    [0, 0, 0, 1, 1, 0, 1],  # 0
    [0, 0, 1, 1, 0, 0, 1],  # 1
    [0, 0, 1, 0, 0, 1, 1],  # 2
    [0, 1, 1, 1, 1, 0, 1],  # 3
    [0, 1, 0, 0, 0, 1, 1],  # 4
    [0, 1, 1, 0, 0, 0, 1],  # 5
    [0, 1, 0, 1, 1, 1, 1],  # 6
    [0, 1, 1, 1, 0, 1, 1],  # 7
    [0, 1, 1, 0, 1, 1, 1],  # 8
    [0, 0, 0, 1, 0, 1, 1]   # 9
]

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, m = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(n)]

    # 암호 코드 탐색
    pw = []
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] == 1:
                pw = arr[i][j-55:j+1]
                break

    # 암호 코드 복호화
    verify_code = []
    for i in range(8):
        a = pw[i*7:(i+1)*7]
        verify_code.append(code.index(a))

    # 올바른 암호코드인지 확인
    check = 0
    for i in range(8):
        if i%2 == 0:
            check += verify_code[i] * 3
        else:
            check += verify_code[i]

    if check % 10 == 0:
        print(sum(verify_code))
    else:
        print(0)

