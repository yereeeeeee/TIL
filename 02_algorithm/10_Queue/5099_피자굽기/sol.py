import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    next_ = [i for i in range(M)]
    on_fire = []
    for j in range(N):
        on_fire.append(next_.pop(0))

    print(f'#{tc}', end=' ')
    while len(on_fire) > 1:
        a = on_fire.pop(0)
        if pizza[a] > 0:
            pizza[a] //= 2
            on_fire.append(a)
        else:
            pizza[a] = 0
            if next_:
                on_fire.append(next_.pop(0))
            continue

    print(int(*on_fire)+1)


    '''def last_pizza(n, pz, s):
        global M
        for i in range(s+1, n):
            if pz[i] <= 0:
                pz[i] = 0
            else:
                pz[i] //= 2
        while n < M:
            for i in range(n):
                if pz[i] <= 0:
                    pz[i] = 0
                    return last_pizza(n+1, pz, i)
                else:
                    pz[i] //= 2

                if sum(pz) == 1:
                    return pz.index(1)+1

    print(last_pizza(N, pizza, 0))'''

'''
    # 초기값 추가
    for i in range(N):
        on_fire[i] = cheese.pop(0)

    while sum(on_fire) > 1:
        for i in range(N):
            if on_fire[i] == 0:
                if cheese:
                    on_fire[i] = cheese.pop(0)
                    cnt += 1
            else:
                on_fire[i] //= 2
        print(on_fire)
'''
