# 모든 자연수는 넷 혹은 그 이하의 제곱수의 합으로 표현할 수 있다.

def check(x, cnt):
    # 제곱수를 순회한다.
    for i in range(n):
        if arr[i] == x:
            return cnt
        elif arr[i] > x:
            return check(x-arr[i-1], cnt+1)

n = int(input())
arr = [i**2 for i in range(n)]
print(check(n, 1))
