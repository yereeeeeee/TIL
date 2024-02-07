import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    S = list(input())
    stack = []
    top = -1

    print(f'#{tc}', end=' ')

    for s in S:
        if s == '{' or s == '(':
            top += 1
            stack.append(s)

        if s == '}':
            try:
                if stack[top] == '{':  # {} 일 때
                    stack.pop()
                    top -= 1
                else:                  # (} 일 때
                    print(0)
                    break
            except:                    # } 일 때
                print(0)
                break
        if s == ')':
            try:
                if stack[top] == '(':  # () 일 때 
                    stack.pop()
                    top -= 1
                else:                  # {) 일 때
                    print(0)
                    break
            except:                    # ) 일 때
                print(0)
                break
    else:                              # ( , { 일 때
        if top != -1:
            print(0)
        else:
            print(1)

    '''
    for s in S:
        if s == '{' or s == '(':
            stack.append(s)
            top += 1
        elif s == '}':
            if top > -1:
                if stack[top] == '{':
                    stack.pop()
                    top -= 1
                else:
                    w += 1
                    break
        elif s == ')':
            if top > -1:
                if stack[top] == '(':
                    stack.pop()
                    top -= 1
                else:
                    w += 1
                    break

    if top != -1:
        print(0)
    elif w == 0:
        print(1)
    else:
        print(0)

    '''
    '''
    for s in S:
        if s == '{' or s == '(':   # stack 예: [{, (, {, (]
            stack.append(s)
            top += 1
    for s in S:                 # S 예: [p, r, i, ..., ), )]
        if s == ')':
            if stack[top] != '(':
                print(0)
                break
            else:
                top -= 1
        elif s == '}':
            if stack[top] != '{':
                print(0)
                break
            else:
                top -= 1
    else:
        print(1)
    '''
