import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = input()
    stack = []
    cnt = 0

    while cnt < N:
        for i in range(len(arr)):
            if arr[i].isdigit():
                stack.append(i)
                cnt += 1
            elif arr[i] == '*':
                stack.append(stack.pop() * arr[i+1])
                # print(stack)
                # print(type(stack))
                cnt += 2
            elif arr[i] == '+':
                cnt += 1
                # stack.append(stack.pop() + sta

    print(stack[0])