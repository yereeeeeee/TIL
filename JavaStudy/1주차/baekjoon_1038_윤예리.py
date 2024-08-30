n = int(input())
if n <= 10: exit(print(n))
value = 10
cnt = 10
visited = [False] * 10

def check(length, target_len, value):
    if length == target_len: return value

    for i in range(10):
        for j in range(0, i):
            pass



