import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    char = list(input())
    for i in range(0, len(char)//2+1):
        if char[i] != char[len(char)-i-1]:
            print(0)
            break
    else:
        print(1)