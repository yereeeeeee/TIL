N = int(input())
P_i = list(map(int, input().split()))

def time(k):
    ls = []
    a = 0
    for i in P_i:
        a += i
        ls.append(a)
    return sum(ls)

