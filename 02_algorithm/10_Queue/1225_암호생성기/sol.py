import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    q = list(map(int, input().split()))

    while 0 not in q:
        for cnt in range(1, 6):
            q_0 = q.pop(0)
            if q_0-cnt > 0:
                q.append(q_0-cnt)
            else:
                q.append(0)
                break

    print(f'#{tc}', end=' ')
    print(*q)