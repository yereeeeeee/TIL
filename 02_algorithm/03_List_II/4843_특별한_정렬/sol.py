import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    a_i = list(map(int, input().split()))

    result = []
    for i in range(5):
        result.append(a_i.pop(a_i.index(max(a_i))))
        result.append(a_i.pop(a_i.index(min(a_i))))
    print(f'#{test_case}', end=' ')
    print(*result)
    
# bubble, counting, selection 으로 풀어보기

