import sys
sys.stdin = open('input.txt')

def post(T):
    if T:
        post(left[T])
        post(right[T])
        if node[T] == 0:        # 값이 비어있고
            if right[T] == 0:   # 오른쪽 자식 없으면
                # stack.append(node[left[T]])
                node[T] = node[left[T]]
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
                node[T] = a+b
        else:
            stack.append(node[T])


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')

    n, m, l = map(int, input().split())
    node = [0] * (n+1)
    left = [0] * (n+1)
    right = [0] * (n+1)
    for i in range(1, n+1):
        l_i = i*2   # 왼쪽 자식
        r_i = i*2+1 # 오른쪽 자식
        if 1<l_i<=n:
            left[i] = l_i
        if 1<r_i<=n:
            right[i] = r_i

    for _ in range(m):
        a, b = map(int, input().split())
        node[a] = b

    stack = []
    post(1)
    # print(node)
    print(node[l])