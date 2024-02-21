import sys
sys.stdin = open('input.txt')

# 후위순회
def postorder(T):
    if T:
        postorder(left[T])
        postorder(right[T])
        stack.append(node[T])
# 계산
def cal(st):
    stack = []
    for s in st:
        if s.isdigit():
            stack.append(s)
        else:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if s == '+':
                stack.append(num1+num2)
            elif s == '-':
                stack.append(num1-num2)
            elif s == '*':
                stack.append(num1*num2)
            else:
                stack.append(num1//num2)
    print(*stack)

for tc in range(1, 11):
    print(f'#{tc}', end=' ')
    n = int(input())

    left = [0] * (n+1)
    right = [0] * (n+1)
    node = [''] * (n+1)
    for i in range(n):
        input_ = list(map(str, input().split()))
        nb = int(input_.pop(0))
        a = input_.pop(0)
        node[nb] = a
        if not a.isdigit():
            left[nb] = int(input_[0])
            right[nb] = int(input_[1])

    stack = []
    postorder(1)
    cal(stack)



