import sys
input = sys.stdin.readline

def dfs(i, memory, value):
    global result

    if memory >= m:
        result = min(result, value)
        return

    if value > result:
        return

    for j in range(i, n):
        dfs(j+1, memory+arr[j], value+cost[j])
        dfs(j+1, memory, value)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = float('inf')
dfs(0, 0, 0)
print(result)