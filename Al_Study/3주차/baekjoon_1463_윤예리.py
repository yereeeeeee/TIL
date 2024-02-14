N = int(input())
cnt = []

# 각 경우를 dfs로 해서
# 제일 짧은 루트 출력
def sol(n):
    global cnt
    ans = []
    if n == 1:
        print(cnt)
    if (n-1)%3 == 0:
        ans.append(n-1)
        sol(n-1)
    if n % 3 == 0:
        ans.append(n//3)
        sol(n//3)
    if n % 2 == 0:
        ans.append(n//2)
        sol(n//2)
    ans.append(n-1)
    cnt.append(ans)
    sol(n-1)

sol(N)