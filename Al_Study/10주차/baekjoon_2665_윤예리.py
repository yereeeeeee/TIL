n = int(input())
arr = []
for i in range(n):
    arr.extend(list(map(int, input().split())))

print(arr)