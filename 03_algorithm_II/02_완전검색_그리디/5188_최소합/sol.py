import sys
sys.stdin = open('input.txt')

di = [1, 0]
dj = [0, 1]

def find(i, j, total):
    global min_value

    stack.append([i, j, total])

    if total > min_value:
        return

    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]

        if ni < n and nj < n:
            if [ni, nj, total] not in stack:
                stack.append([ni, nj, total])
                total += arr[ni][nj]
                find(ni, nj, total)
                total -= arr[ni][nj]
                stack.pop()

    return total

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    stack = []
    min_value = 300

    print(find(0, 0, arr[0][0]))