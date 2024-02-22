from itertools import combinations
n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        s[i][j] += s[j][i]
        s[j][i] = 0

ls = []
for i in range(n):
    for j in range(n):
        if s[i][j] != 0:
            ls.append(s[i][j])

comb = list(combinations(ls, n))
min_v = 100
for i in range(len(comb)):
    if min_v> abs(comb[i][0]-comb[i][1]):
        print(comb[i])
        min_v=abs(comb[i][0]-comb[i][1])
print(min_v)