import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    K, N, M = map(int, input().split())
    M_i = list(map(int, input().split()))
    stop = [0] * (N+1)
    for m in M_i:
        stop[m] = m

    n = 0           # 버스의 현재 위치
    result = []     # 버스가 지나친 정류장 list
    while n < N-K:  # N-K 이후에 출발하면 무조건 도착
        out = []
        # n에서 출발한 버스가 n+k까지 가면서 만나는 충전소를 out에 저장
        for j in range(n+1, n+K+1):
            out.append(stop[j])
            s = sum(out)

        # 충전소를 못 만나면 0을 출력
        if s == 0:
            print(f'#{test_case} 0')
            n = 999999              # 이 경우는 끝났기 때문에 이후에 고려되면 안됨
            break
        elif len(set(out)) == 2:    # 버스가 만나는 정류장이 1개 일 때,
            n = s
        else:                       # 버스가 만나는 정류장이 2개 이상일 때,
            n = max(out)

        result.append(n)
    if n != 999999:
        print(f'#{test_case} {len(result)}')
