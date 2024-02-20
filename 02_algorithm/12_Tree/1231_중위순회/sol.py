import sys
sys.stdin = open('input.txt')

def inorder(T):
    if T:
        inorder(left[T])
        print(node[T], end='')
        inorder(right[T])

for tc in range(1, 11):
    print(f'#{tc}', end=' ')
    N = int(input())
    left = [0] * (N+1)
    right = [0] * (N+1)
    node = [''] * (N+1)

    for n in range(N):
        ls = list(map(str, input().split())) # 1 W 2 3
        num = ls.pop(0) # 1
        char = ls.pop(0) # W
        node[int(num)] = char

        if ls:
            left_child = ls.pop(0) # 2
            left[int(num)] = int(left_child) # left[1] = 2
        if ls:
            right_child = ls.pop(0) # 3
            right[int(num)] = int(right_child) # right[1] = 3

    inorder(1)
    print()



