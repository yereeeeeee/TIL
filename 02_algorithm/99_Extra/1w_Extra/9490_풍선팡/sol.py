import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    for i in range(0, N):
        for j in range(0, M):
            total = 0
            total += A[i][j]

            # 오른쪽
            for m in range(1, A[i][j]+1):
                if 0 <= i < N and 0 <= j+m < M:
                    total += A[i][j+m]
                # print('우:', total)
            # 왼쪽
            for m in range(1, A[i][j] + 1):
                if 0 <= i < N and 0 <= j-m < M:
                    total += A[i][j-m]
                # print('좌:', total)
            # 위
            for m in range(1, A[i][j] + 1):
                if 0 <= i-m < N and 0 <= j < M:
                    total += A[i-m][j]
                # print('상:', total)
            # 아래
            for m in range(1, A[i][j] + 1):
                if 0 <= i+m < N and 0 <= j < M:
                    total += A[i+m][j]
                # print('하:', total)

            if max_value < total:
                max_value = total
            # print(i, total)

    print(f'#{test_case} {max_value}')