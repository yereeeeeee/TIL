import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    P, A, B = map(int, input().split())

    l = 1
    r = P

    cnt_a = 0
    # A 탐색
    while l <= r:
        c = int((l + r) / 2)
        cnt_a += 1
        if c == A:
            break
        elif c > A:
            r = c
        else:
            l = c

    # 초기화
    l = 1
    r = P

    cnt_b = 0
    #  B 탐색
    while l <= r:
        c = int((l + r) / 2)
        cnt_b += 1
        if c == B:
            break
        elif c > B:
            r = c
        else:
            l = c

    # 승자 출력
    if cnt_a > cnt_b:
        print(f'#{test_case} B')
    elif cnt_a < cnt_b:
        print(f'#{test_case} A')
    else:
        print(f'#{test_case} 0')

    # 탐색하는 반복문을 함수로 바꾸어서 사용가능함.
    # 재귀함수로 바꿀 수도 있음.