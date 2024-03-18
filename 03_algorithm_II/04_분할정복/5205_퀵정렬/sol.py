import sys
sys.stdin = open('input.txt')

def quickSort(l, r):
    if l < r:
        s = partition(l, r)
        quickSort(l, s-1)
        quickSort(s+1, r)


def partition(l, r):
    p = a[l]
    i = l
    j = r
    while i <= j:
        while i <= j and a[i] <= p:
            i += 1
        while i <= j and a[j] >= p:
            j -= 1

        if i < j:
            a[i], a[j] = a[j], a[i]

    a[l], a[j] = a[j], a[l]
    return j

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n = int(input())
    a = list(map(int, input().split()))

    quickSort(0, n - 1)
    print(a[n//2])