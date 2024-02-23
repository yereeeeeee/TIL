# import sys
# sys.stdin = open('input.txt')
'''
1. 조합에 1이 있음 -> 1을 무조건 부모로 둔다.
2. 왼쪽이 부모가 있음 -> 오른쪽이 자식
3. 오른쪽이 부모가 있음 -> 왼쪽이 자식
'''
def mktr(i, j):
    if i == 1:
        par[j] = 1
    elif j == 1:
        par[i] = 1
    else:
        if par[i] != 0:
            par[j] = i
        elif par[j] != 0:
            par[i] = j

# 트리의 루트는 1
n = int(input())
par = [0] * (n+1)
ls = []
for _ in range(n-1):
    p, c = map(int, input().split())
    ls.append((p, c))

# 정렬해서 트리 생성
for i in sorted(ls):
    mktr(i[0], i[1])

# 만약 부모가 없는 노드가 있다면 다시 한번 더 확인
for i in range(1, n+1):
    if par[i] == 0:
        for j in ls:
            if j[0] == i or j[1] == i:
                mktr(j[0], j[1])

for i in range(2, n+1):
    print(par[i])