# 시간초과
n, k = map(int, input().split())

jewels = []
for _ in range(n):
     jewels.append(list(map(int, input().split())))

bags = []
for _ in range(k):
    bags.append(int(input()))

jewels.sort(key=lambda x:(-x[1], x[0]))     # 가격이 큰 순으로 정렬, 가격이 같다면 무게가 가벼운 순으로 정렬
bags.sort()

i = 0
result = 0
while i < k:
    for j in range(len(jewels)):
        if bags[i] >= jewels[j][0]:
            result += jewels.pop(j)[1]
            i += 1
            break
    else:
        i += 1

print(result)
