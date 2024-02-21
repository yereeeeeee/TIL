import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, m, k = map(int, input().split())
    arr_sec = list(map(int, input().split()))
    sec = max(arr_sec)
    bread = [0] * (sec+1)


    for i in range(1, sec+1):
        if i % m == 0:
            bread[i] = k*(i//m)
        else:
            bread[i] = bread[i-1]

    print(bread)

    for i in arr_sec:
        if bread[i] < 1:
           print('Impossible')
           break
        else:
            for j in range(i+1):
                bread[j] -= 1
    else:
        print('Possible')