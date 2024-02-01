import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    # 연속된 1은 합쳐져서 num이라는 list로 나옴
    # 행 별 0을 기준으로 split
    for i in range(N):
        num = []
        word = 0
        for j in range(N):
            if arr[i][j] == 1:
                if j == N-1:
                    word += 1
                    num.append(word)
                else:
                    word += 1
            elif arr[i][j] == 0:
                num.append(word)
                word = 0

        for n in num:
            if K == n:
                cnt += 1

    # 열 별 0을 기준으로 split
    for i in range(N):
        num = []
        word = 0
        for j in range(N):
            if arr[j][i] == 1:
                if j == N - 1:
                    word += 1
                    num.append(word)
                else:
                    word += 1
            elif arr[j][i] == 0:
                num.append(word)
                word = 0

        for n in num:
            if K == n:
                cnt += 1

    print(f'#{test_case} {cnt}')






