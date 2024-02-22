'''
1. 첫 줄에 도착한 사분면 번호를 좌표값으로 계산한다.
2. 이동시킨다.
3. 이동한 좌표의 사분면 번호를 계산한다.
'''

# 조각 위치 찾는 함수
def pos(n, i, j):
    # print(i, j)
    if len(i) == 1:
        return i[0], j[0]
    a = int(n.pop(0))
    if a == 1:      # 1사분면
        new_i = i[:(len(i)//2)]
        new_j = j[(len(j)//2):]
    elif a == 2:    # 2사분면
        new_i = i[:(len(i)//2)]
        new_j = j[:(len(j)//2)]
    elif a == 3:    # 3사분면
        new_i = i[(len(i)//2):]
        new_j = j[:(len(j)//2)]
    else:           # 4사분면
        new_i = i[(len(i)//2):]
        new_j = j[(len(j)//2):]

    return pos(n, new_i, new_j)

# 사분면 찾는 함수
def find(n, i, j):
    if n == i+j:
        return
    else:
        if n[0] in i[:(len(i)//2)] and n[1] in j[(len(j)//2):]: # 1사분면
            print(1, end='')
            find(n, i[:(len(i)//2)], j[(len(j)//2):])
        elif n[0] in i[:(len(i)//2)] and n[1] in j[:(len(j)//2)]:
            print(2, end='')
            find(n, i[:(len(i)//2)], j[:(len(j)//2)])
        elif n[0] in i[(len(i)//2):] and n[1] in j[:(len(j)//2)]:
            print(3, end='')
            find(n, i[(len(i)//2):], j[:(len(j)//2)])
        else:
            print(4, end='')
            find(n, i[(len(i)//2):], j[(len(j)//2):])


d, quad = map(int, input().split())
x, y = map(int, input().split())
arr = [[0] * (2**d) for _ in range(2**d)]
ls_x = [i for i in range(1, 2**d+1)]
ls_y = [i for i in range(1, 2**d+1)]
q = list(str(quad))

#print(pos(q, ls_x, ls_y))
p = list(pos(q, ls_x, ls_y))
# 이동
p[0] -= y
p[1] += x
find(p, ls_x, ls_y)


