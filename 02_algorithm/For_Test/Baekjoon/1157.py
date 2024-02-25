string = list(input().upper())
d = {}
for s in string:
    d[s] = 0
for s in string:
    d[s] += 1
cnt = list(d.values())
max_num = cnt.count(max(cnt))
if max_num > 1:
    print('?')
else:
    for s in string:
        if d[s] == max(cnt):
            print(s)
            break