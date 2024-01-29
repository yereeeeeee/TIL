import sys
sys.stdin = open('input.txt')

for _ in range(10):
    N = int(input())
    apt = list(map(int, input().split()))
    view = 0

    for a in range(2, len(apt)-2):
        b = [apt[a-2], apt[a-1], apt[a+1], apt[a+2]]
        if apt[a] > max(b):
            view += (apt[a] - max(b))
    print(f'#{_+1} {view}')