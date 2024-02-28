import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, m = map(int, input().split())
    w = sorted(list(map(int, input().split())), reverse=True)     # 화물 무게
    t = sorted(list(map(int, input().split())), reverse=True)     # 적재 용량

    result = 0
    for i in range(m):          # 트럭
        j = 0
        while w and j < len(w):         # 화물을 순회하면서
            if t[i] >= w[j]:            # 화물 보다 트럭 용량이 더 크면
                result += w.pop(j)      # 담아주고
                break
            else:                       # 아니면 다음 화물 확인
                j+=1
    print(result)


