import sys
sys.stdin = open('input.txt')

for test_case in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for d in range(dump):
        h = box.index(max(box))
        l = box.index(min(box))
        box[h] -= 1
        box[l] += 1

    print(f'#{test_case} {max(box)-min(box)}')