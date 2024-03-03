def per(result = [], i = 0):
    if len(result) == m:
        print(*result)
        return

    if i < len(arr):
        per(result+[arr[i]], i+1)
        per(result, i+1)

n, m = map(int, input().split())
arr = sorted(list(set(map(int, input().split()))))
per()