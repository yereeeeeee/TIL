import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a_i = list(map(int, input().split()))

    def BubbleSort(a, n):
        for i in range(n-1, -1, -1):
            for j in range(i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
        return a

    std = BubbleSort(a_i, len(a_i))
    print(std)
    result = []
    for m in range(5):
        result.append(std.pop())
        result.append(std.pop(0))
    print(f'#{test_case}', end=' ')
    print(*result)


