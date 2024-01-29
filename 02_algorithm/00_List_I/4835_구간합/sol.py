import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    a_i = list(map(int, input().split()))

    for m1 in range(M):
        arr = []
        sum = 0
        for m in range(M):
            sum += a_i[m]
        arr.append(sum)
    print(arr)


    #print(f'#{t+1} {max(a_j) - min(a_j)}')