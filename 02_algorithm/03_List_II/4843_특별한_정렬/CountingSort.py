import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a_i = list(map(int, input().split()))

    # 1번
    cnt = []
    for _ in range(max(a_i)+1):
        cnt.append(0)

    for i in a_i:
        cnt[i] += 1

    temp = []
    for c in range(len(cnt)):
        while cnt[c] > 0:
            temp.append(c)
            cnt[c] -= 1

    # 2번
    def CountingSort(DATA, TEMP, k):
        # DATA: 입력 배열
        # TEMP: 정렬된 배열
        # COUNTS: 카운트 배열

        COUNTS = [0] * (k+1)

        for i in range(0, len(DATA)):
            COUNTS[DATA[i]] += 1

        for i in range(1, k+1):
