import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    card = list(map(int, input().split()))

    def tournament(start, end):
        # 하나 남을 때 까지 쪼갠다.
        # 하나 남으면 남은 원소의 index를 return
        if start == end:
            return start

        mid = (start+end) // 2
        left = tournament(start, mid)
        right = tournament(mid+1, end)

        # return 받은 값을 가지고 가위바위보
        winner = (card[left] - card[right]) % 3
        if winner == 2:
            return right
        else:
            return left

    result = tournament(0, N-1)
    print(result+1)


