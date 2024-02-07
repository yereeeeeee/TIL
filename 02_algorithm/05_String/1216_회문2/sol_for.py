import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    test_case = int(input())
    length = 100
    arr = [list(input()) for _ in range(100)]
    result = 0

    while length > 1:
        if result:
            break
        # 행 검사
        for i in range(100):
            for k in range(100 - length + 1):
                cnt = 0
                if result:
                    break
                for j in range(length // 2):
                    if arr[i][j+k] == arr[i][length-j-1+k]:
                        cnt += 1
                if cnt >= length//2:
                    print(f'#{tc} {length}')
                    result += 1
                    break
            if result > 0:
                break

        # 열 검사
        for j in range(100):
            for k in range(100 - length + 1):
                cnt = 0
                if result:
                    break
                for i in range(length // 2):
                    if arr[i+k][j] == arr[length-i-1+k][j]:
                        cnt += 1
                if cnt >= length//2:
                    print(f'#{tc} {length}')
                    result += 1
                    break
            if result > 0:
                break

        length -= 1
    else:
        print(f'#{tc} 1')

