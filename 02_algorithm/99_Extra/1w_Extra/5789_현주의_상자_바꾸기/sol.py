import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N, Q = map(int, input().split())

    box = []  # 빈 박스
    for n in range(N):
        box.append(0)

    for q in range(1, Q+1):
        L, R = map(int, input().split())
        for a in range(L-1, R):             # 리스트에 넣기 때문에 한 칸씩 앞으로 간 range를 범위로 지정
            box[a] = q

    print(f'#{test_case}', end=' ')
    print(*box)