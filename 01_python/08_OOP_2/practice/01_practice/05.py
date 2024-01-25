a = int(input())
def sig(x):
    if x == 1:
        return 1
    else:
        return x + sig(x-1)
print(sig(a))
