import sys
sys.stdin = open('input.txt')

k = int(input())    # 1m^2 당 자라는 참외의 수
ls = []
left_right = []
up_down = []

while 1:            # 값 받아오기
    try:
        direction, distance = map(int, input().split())
        ls.append([direction, distance])
    except:
        break

for i in ls:
    if i[0] == 1 or i[0] == 2:      # 동쪽 / 서쪽
        left_right.append(i)
    else:                           # 북쪽 / 남쪽
        up_down.append(i)

total = (max(left_right, key=lambda x : x[1])[1])*(max(up_down, key=lambda x : x[1])[1])
print(ls)


