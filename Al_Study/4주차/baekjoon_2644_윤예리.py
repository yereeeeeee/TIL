n = int(input())
arr = [[] for _ in range(n+1)]
print(arr)
a, b = map(int, input().split())
m = int(input())
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)    # 부자관계 그래프
    arr[y].append(x)

stack = [arr[a]]
top = -1
while stack:
    