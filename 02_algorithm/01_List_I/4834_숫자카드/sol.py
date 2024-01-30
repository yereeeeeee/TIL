import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    a_i = list(map(int, list(input())))
    b_i = [0] * 10
    count_ls = []
    for i in a_i:
        b_i[i] = a_i.count(i)

    b_i.reverse() # 큰 값 찾기
    print(f'#{test_case} {9 - b_i.index(max((b_i)))} {max(b_i)}')

