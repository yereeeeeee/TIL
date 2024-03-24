def cnt(x):


score = []
n = int(input())
for _ in range(n):
    score.append(int(input()))

score.pop(score.index(max(score)))
score.pop(score.index(min(score)))

print(score)