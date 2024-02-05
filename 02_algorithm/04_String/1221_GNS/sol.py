import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    test_case, length = map(str, input().split())
    char = list(input().split())
    num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    cnt = [0] * 10

    for i in char:
        cnt[num.index(i)] += 1

    print(test_case)
    for i in range(10):
        for j in range(cnt[i]):
            print(num[i], end=' ')