def find(x):
    if parents[x] == x:
        return x

    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x < y:
        parents[y] = x
    else:
        parents[x] = y

n, m = map(int, input().split())
arr, edges = [], []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))
parents = [i for i in range(n+1)]

#https://www.acmicpc.net/board/view/121067