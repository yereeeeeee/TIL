import sys
sys.stdin = open('input.txt')

n = int(input())
dice_ls = []
for i in range(n):
    dice = list(map(int, input().split()))
    dice_ls.append(dice)

for i in range(6):
    if i == 0:  # A 면이 가장 아랫면일때
        for j in dice_ls:





