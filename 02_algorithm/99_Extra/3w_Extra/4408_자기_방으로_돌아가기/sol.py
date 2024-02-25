import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())

    arr = []
    for n in range(N):
        now, togo = map(int, input().split())
        route = [i for i in range(now, togo+1)]
        arr.append(route)

    result = 1
    for i in range(n-1):
        for j in range(i+1, n):
            a = list(set(arr[i]) & set(arr[j]))
            print(a)
            if a == []:
                pass
            else:
                result += 1
    print(result)