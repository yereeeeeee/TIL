a = [1, 2, 3, 4, 5]
v = [0] * 5
idx = [0, 1, 2, 3, 4]

def bt(arr):
    if len(arr) == 5:
        print(arr)
        return

    for j in idx:
        if not v[j]:
            v[j] = 1
            bt(arr + [a[j]])
            v[j] = 0

bt([])
