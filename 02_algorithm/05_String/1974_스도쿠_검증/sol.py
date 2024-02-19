import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    arr = [list(map(int, input().split())) for _ in range(9)]

    def sdoku():
        for i in range(9):
            for j in range(9):
                if j not in arr[i]:
                    return 0

