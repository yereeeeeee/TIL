from pprint import pprint
m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]

# graph
for _ in range(k):
    a1, b1, a2, b2 = map(int, input().split())
    for i in range(m-b2, m-b1):
        for j in range(a1, a2):
            arr[i][j] = 1
pprint(arr)

cnt = 0
area = []

def dfs(r, c):
