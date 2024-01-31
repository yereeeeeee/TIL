import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    max_value = 0                        # 최대값
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for m in range(i, i+M):     # M*M 범위를 순회하며 total에 더함
                for n in range(j, j+M):
                    total += arr[m][n]
            if total > max_value:
                max_value = total       # 최대값 찾기
    print(f'#{test_case} {max_value}')
