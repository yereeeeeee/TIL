import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    s = list(input())
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i+1]:
            s.pop(i)
            s.pop(i)
            i = 0
        else:
            i += 1
    print(f'#{tc} {len(s)}')
    
# stack으로 풀어보기