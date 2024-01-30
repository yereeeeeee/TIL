import sys
sys.stdin = open('input.txt')

numbers = [2, 3, 5, 7, 11]
T = int(input())
for test_case in range(1, T+1):
    N = int(input())

    result = []
    for n in numbers:
        i = 0

        while N % n == 0:
            N /= n
            i += 1
        result.append(i)
    print(f'#{test_case}', end=' ')
    print(*result)
