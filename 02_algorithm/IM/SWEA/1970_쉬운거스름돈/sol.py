import sys
sys.stdin = open('input.txt')

change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}')
    n = int(input())
    cnt = [0] * 8

    for c in range(len(change)):
        cnt[c] = n // change[c]
        n %= change[c]
        # 아래 코드 왜 안되는지 모르겠음
        # 아 ㅋㅋ #tc 밑에 띄어쓰기.....ㅋㅋㅋㅋ
        # while change[c] <= n:
        #     n -= change[c]
        #     cnt[c] += 1
    print(*cnt)