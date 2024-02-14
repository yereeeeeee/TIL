import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    length = int(input())
    problem = list(input())

    # 후위 표기식
    stack = []
    top = -1
    result = []
    for char in problem:
        if char == '+':
            while stack:
                result.append(stack.pop())
                top -= 1
            stack.append(char)
            top += 1
        elif char == '*':
            while stack and stack[top] != '+':
                result.append(stack.pop())
                top -= 1
            stack.append(char)
            top += 1
        else:
            result.append(char)
    while stack:
        result.append(stack.pop())

    print(result)
    # 계산
    stack2 = []
    for char in result:
        if char.isdigit():
            stack2.append(char)
        else:
            num2 = int(stack2.pop())
            num1 = int(stack2.pop())
            if char == '+':
                stack2.append(num1+num2)
            else:
                stack2.append(num1*num2)

    print(f'#{tc} {stack2[0]}')
