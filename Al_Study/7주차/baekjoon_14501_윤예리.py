'''
dp
'''
n = int(input())
dp = [0] * (n+1)

schedule = []
for _ in range(n):
    t, p = map(int, input().split())
    schedule.append((t, p))

print(schedule)