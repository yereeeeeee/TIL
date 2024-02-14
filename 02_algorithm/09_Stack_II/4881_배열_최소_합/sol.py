import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_v = 30
    P = [i for i in range(N)]

    # 순열
    def f(i, k):
        global min_v
        if i == k:  # 순열이 완성 되었을 때
            s = 0   # 선택한 원소의 합
            for j in range(k):  # j 행에 대해
                if s < min_v:
                    s += arr[j][P[j]]  # j 행에서 P[j] 열을 고른 경우의 합 구하기
                else:
                    break
            if s < min_v:
                min_v = s

        else:
            for j in range(i, k):  # P[i] 자리에 올 원소 P[j]
                P[i], P[j] = P[j], P[i]
                f(i + 1, k)
                P[i], P[j] = P[j], P[i]  # 교환 전으로 복구

    f(0, N)
    print(f'#{tc} {min_v}')