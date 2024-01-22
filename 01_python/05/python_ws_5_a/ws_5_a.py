N = 9
data_1 = '123456789'
arr_1 = []
# 아래에 코드를 작성하시오.
dt_list = list(data_1)
for n in range(N):
    arr_1.append(dt_list[n])
print(arr_1)

M = 15
data_2 = '1 2 3 4 5 6 7 8 9 10 11 12 13 14 15'
# 아래에 코드를 작성하시오.
arr_2 = []
dt_split = data_2.split(' ')
for m in range(M):
    if int(dt_split[m]) % 2 == 0:
        continue
    else: print(dt_split[m])

