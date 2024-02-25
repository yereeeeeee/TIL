a, b = map(str, input().split())
c = int(a[::-1])
d = int(b[::-1])
print(max(c, d))