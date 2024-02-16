n = int(input())
# 행은 집
# 열은 색
arr = [list(map(int, input().split())) for _ in range(n)]

min_v = []
for i in range(n):
    min_v.append(min(arr[i]))

# 최소값을 가지는 행, 열
r = min_v.index(min(min_v))
c = arr[r].index(min(arr[r]))

cost = arr[r][c]
for i in range(r, n):
    if arr[i].index(min(arr[i])) != c:
        cost += min(arr[i])
    else:
        arr[]
