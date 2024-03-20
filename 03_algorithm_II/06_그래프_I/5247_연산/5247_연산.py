import sys
sys.stdin = open('input.txt')
from collections import deque

# bfs
# depth가 root에 가까울 수록 정답인데 왜 dfs를 먼저 생각했지;
def bfs(v, d):
    q = deque([(v, d)])
    visited = [0] * 1000001
    visited[v] = 1

    while q:
        t, d = q.popleft()
        if t == m:
            print(d)
            return

        for next_ in [t+1, t-1, t*2, t-10]:
            if 0 < next_ < 1000001 and not visited[next_]:
                q.append((next_, d+1))
                visited[next_] = 1

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, m = map(int, input().split())
    bfs(n, 0)




# dfs 안됨
# '''
# +1, -1, *2, -10
# dp = 2에서 3 만드는 횟수, 4 만드는 횟수, ..., 7 만드는 횟수
# '''
# cal = [0, 1, 2, 3]
# def dfs(d, value, key):
#     global result
#     if value == key:
#         result = d
#         return
#
#     if d >= dp[i] or d >= result:
#         return
#
#     if value > 1000000 or value < 1:
#         return
#
#     for a in cal:
#         if a == 0:
#             dfs(d+1, value+1, key)
#         elif a == 1:
#             dfs(d+1, value-1, key)
#         elif a == 2:
#             dfs(d+1, value*2, key)
#         else:
#             dfs(d+1, value-10, key)
#
# T = int(input())
# for tc in range(1, T+1):
#     print(f'#{tc}', end=' ')
#
#     n, m = map(int, input().split())
#     dp = [0] * (m+1)
#     for i in range(n, m+1):
#         dp[i] = dp[i-1] + 1     # 최악의 경우
#         result = float('inf')
#         dfs(0, n, i)
#         dp[i] = min(result, dp[i])
#     # print(dp)
#     print(dp[m])






# dfs 왜 안될까
# def dfs(d, value):
#     global result
#
#     if value == m:
#         if result > value:
#             result = value
#         return
#
#     if value > 1000000 or value <= 0:
#         return
#
#     if d >= result:
#         return
#
#     for a in cal:
#         if a == 0:
#             dfs(d+1, value+1)
#         elif a == 1:
#             dfs(d+1, value-1)
#         elif a == 2:
#             dfs(d+1, value*2)
#         else:
#             dfs(d+1, value-10)
#
# T = int(input())
# for tc in range(1, T+1):
#     print(f'#{tc}', end=' ')
#
#     n, m = map(int, input().split())
#     cal = [0, 1, 2, 3]
#
#     result = 1000000
#     dfs(0, n)
#     print(result)
