import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a_i = list(map(int, input().split()))

    def SelectionSort(a, n):
        for i in range(n-1):
            min_idx = i
            for j in range(i+1, n):
                if a[min_idx] > a[j]:
                    min_idx = j
            a[i], a[min_idx] = a[min_idx], a[i]
        return a

    print(SelectionSort(a_i, N))



