import sys
sys.stdin = open('input.txt')

def merge(left, right):
    result = []
    global cnt
    if left[-1] > right[-1]:
        cnt += 1

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:

            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))
    return result

def merge_sort(m):
    if len(m) == 1:
        return m

    left = []
    right = []
    middle = len(m) // 2

    for i in range(middle):
        left.append(m[i])
    for j in range(middle, len(m)):
        right.append(m[j])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    tmp = merge_sort(a)

    print(tmp[n//2], end=' ')
    print(cnt)