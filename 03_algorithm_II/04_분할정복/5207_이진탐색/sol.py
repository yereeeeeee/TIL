import sys
sys.stdin = open('input.txt')

def binarySearch(key, section):
    low = 0
    high = n-1
    global result

    while low <= high:
        mid = low + ((high - low) // 2)

        if a[mid] == key:
            result += 1
            return mid
        elif a[mid] > key and section != 1:
            high = mid - 1
            section = 1
        elif a[mid] < key and section != 2:
            low = mid + 1
            section = 2
        else:
            return
    return

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    result = 0

    a.sort()
    for i in b:
        binarySearch(i, 0)

    print(result)