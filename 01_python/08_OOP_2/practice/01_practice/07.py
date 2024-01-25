N = int(input())
b = []
for n in range(1, N+1):
    a = list(map(int, input().split()))
    b.append(sum(a))
print(sum(b))
