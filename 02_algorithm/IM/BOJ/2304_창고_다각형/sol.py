import sys
sys.stdin = open('input.txt')

# 왼쪽
def find_top_left(i, a):
    global result

    new_a = a[:i]       # max값 왼쪽
    if not new_a:
        return

    j = new_a.index(max(new_a))
    if max(new_a) == 0:
        return
    else:
        result += max(new_a) * (i - j)
        find_top_left(j, new_a)


# 오른쪽
def find_top_right(i, a):
    global result

    new_a = a[i:]
    #print(new_a)
    if not new_a:
        return
    j = new_a.index(max(new_a))
    if max(new_a) == 0:
        return
    else:
        result += max(new_a) * (j-i)
        find_top_right(j, new_a)


n = int(input())
ls = []
L = []
for _ in range(n):
    l, h = map(int, input().split())
    ls.append([l, h])
    L.append(l)

arr = [0] * (max(L)+1)

for i in ls:
    arr[i[0]] = i[1]
print(arr)


top = arr.index(max(arr))
result = max(arr)

find_top_left(top, arr)
find_top_right(top+1, arr)

#print(result)



