'''
min(제일 낮은 높이 ~ 제일 높은 높이만큼 맞추기)
'''
from copy import deepcopy

def build(arr, height, b2):
    global result

    time = 0

    for i in range(n):
        for j in range(m):
            if time > min(result, key=lambda x:x[0])[0]:
                return

            # 1번 작업
            if arr[i][j] > height:
                r = arr[i][j] - height
                arr[i][j] = height
                b2 += r
                time += 2*r

            # 2번 작업
            if arr[i][j] < height:
                r = height - arr[i][j]
                if b2 >= r:
                    arr[i][j] = height
                    b2 -= r
                    time += r
                else:
                    return
    else:
        result.append([time, height])

# 파서 쌓는 경우 고려 필요
n, m, b = map(int, input().split())
ground = []
max_height = 0
min_height = 256
for _ in range(n):
    ls = list(map(int, input().split()))
    max_height = max(max_height, max(ls))
    min_height = min(min_height, min(ls))
    ground.append(ls)
result = [[float('INF'), 257]]

min_time = float('inf')

for k in range(min_height, max_height+1):
    build(deepcopy(ground), k, deepcopy(b))
    current = result[-1][0]
    if min_time >= current:
        min_time = current
        height = result[-1][1]

print(min_time, height)
# result.sort(key=lambda x:(x[0], -x[1]))
# print(*result[0])