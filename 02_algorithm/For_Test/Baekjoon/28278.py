n = int(input())
com = []
stack = []
for _ in range(n):
    a = list(map(int, input().split()))
    com.append(a)
for i in range(n):
    x = com[i][0]
    if x == 1:
        stack.append(com[i][1])
    elif x == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif x == 3:
        print(len(stack))
    elif x == 4:
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)
