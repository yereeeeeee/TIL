# 감소하는 수라면 True 아니라면 False를 반환하는 함수
def check(num):
    string = str(num)
    for s in range(len(string)-1):
        if int(string[s]) <= int(string[s+1]):
            return False
    else:
        return True

def solution(value, d, cnt):
    if value > 9876543210: exit(print(-1))
    if cnt == n: return value

    for i in range(1, 10):



n = int(input())
if n <= 10: exit(print(n))
solution(10, 1, 10)
print()