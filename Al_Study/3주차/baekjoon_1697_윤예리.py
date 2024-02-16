sb, sis = map(int, input().split())
find = [sb]
bf = []

while sis not in find:
    i = find.pop(0)
    find.append(i*2)
    find.append(i+1)
    find.append(i-1)
    bf.append(i)
print(bf)
print(find)

