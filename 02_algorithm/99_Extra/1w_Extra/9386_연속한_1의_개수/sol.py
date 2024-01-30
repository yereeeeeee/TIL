import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    seq = list(input())

    if '1' not in seq:
        result = 0
    else:
        max_num = 1
        num_ls = []
        for s in range(len(seq)-1):
            if int(seq[s]) == 1:
                if int(seq[s+1]):
                    if s+1 == N-1:
                        max_num += 1
                        num_ls.append(max_num)
                    else: max_num += 1
                elif int(seq[s+1]) == 0:
                    num_ls.append(max_num)
                    max_num = 1
        print(f'#{test_case} {max(num_ls)}')