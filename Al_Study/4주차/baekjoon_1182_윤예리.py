n, s = map(int, input().split())
ls = list(map(int, input().split()))

# 순차적으로 포함 되고 안되고
subsets = [[]]
for i in ls:
    L = len(subsets)
    for l in range(L):
        subsets.append(subsets[l] + [i])

cnt = 0
for set in subsets:
    if sum(set) == s  :
        cnt += 1

print(subsets)
print(cnt)
