ls = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
alpha = input()
cnt = 0
for i in ls:
    cnt += alpha.count(i)
print(len(alpha) - cnt)