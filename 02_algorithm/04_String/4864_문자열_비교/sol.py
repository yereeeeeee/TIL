import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr1 = input()
    arr2 = input()
    print(f'#{tc}', end=' ')
    if arr1 in arr2:
        print(1)
    else:
        print(0)