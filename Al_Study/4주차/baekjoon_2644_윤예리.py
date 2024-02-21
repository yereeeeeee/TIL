import sys
sys.stdin = open('input.txt')

def dfs(i, j):
    global cnt
    visited[i] = 1
    if j in ch[i]:
        result.append(cnt)
        return
    for c in ch[i]:
        if visited[c] == 0:
            cnt += 1
            dfs(c, j)


n = int(input())
a, b = map(int, input().split())
m = int(input())

# 그래프 그리기
ch = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    p, c = map(int, input().split())
    ch[p].append(c)
    ch[c].append(p)

cnt = 1
result = []
dfs(a, b)
if result:
    print(*result)
else:
    print(-1)


