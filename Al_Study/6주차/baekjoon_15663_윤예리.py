def per(result = [], i = 0):
    if len(result) == m:
        if result in total:
            pass
        else:
            total.append(result)
        return

    if i < len(arr):
        per(result+[arr[i]], i+1)
        per(result, i+1)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
total = []

for i in range(n):
    per()
    arr.append(arr.pop(0))

for t in sorted(total):
    print(*t)
