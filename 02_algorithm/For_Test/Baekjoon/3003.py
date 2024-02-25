# 킹, 퀸, 룩, 비숍, 나이트, 폰
right_piece = [1, 1, 2, 2, 2, 8]
wrong_piece = list(map(int, input().split()))

for i in range(6):
    print(right_piece[i] - wrong_piece[i], end=' ')