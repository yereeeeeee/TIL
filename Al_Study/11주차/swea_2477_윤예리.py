import sys
input = sys.stdin.readline
from collections import deque
sys.setrecursionlimit(10**9)

def move(t):
    if t > max(tk, key=lambda x:x[1])[1] and not waiting1 and not waiting2:
        return

    # 도착한 손님 reception 대기
    for k in tk:
        if k[1] == t:
            waiting1.append(k[0])

    # 대기 손님 있으면
    if waiting1:
        # reception_desk 순회
        for i in range(n):
            if not reception_desk[i]:
                reception_desk[i] = a[i]
                receptions[i].append(waiting1.popleft())
            elif reception_desk[i] == 1:
                waiting2.append(reception_desk[i])
                reception_desk[i] = 0
            else:
                reception_desk[i] -= 1
    else:
        for i in range(n):
            if reception_desk[i] == 1:
                waiting2.append(reception_desk[i])
                reception_desk[i] = 0
            else:
                reception_desk[i] -= 1

    if waiting2:
        # repair_desk 순회
        for j in range(m):
            if not repair_desk[j]:
                repair_desk[j] = b[j]
                repairs[j].append(waiting2.popleft())
            elif repair_desk[j] == 1:
                repair_desk[j] = 0
            else:
                repair_desk[i] -= 1
    else:
        for j in range(m):
            if repair_desk[j] == 1:
                repair_desk[j] = 0
            else:
                repair_desk[j] -= 1

    return move(t+1)


T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    n, m, k, a, b = map(int, input().split())
    ai = list(map(int, input().split()))
    bj = list(map(int, input().split()))
    tk = deque(list(enumerate(map(int, input().split()), start=1)))
    
    # reception 대기
    waiting1 = deque([])
    # repair 대기
    waiting2 = deque([])

    # 남은 시간 저장
    reception_desk = [0] * n
    repair_desk = [0] * m

    # 다녀갔던 사람들 저장
    receptions = [[] for _ in range(n)]
    repairs = [[] for _ in range(m)]

    move(tk[0][1])
    print(receptions)
    print(repairs)
    result = set(receptions[a-1]) & set(repairs[b-1])
    print(result)

# def reception():
#     # receptions 순회
#     for i in range(n):
#         if not tk:
#             return
#
#         # 비었으면 채운다.
#         if not receptions[i]:
#             k = tk.popleft()
#             reception_desk[i].append(k[0])
#             receptions[i] = [k, ai[i]]
#
#         else:
#             # 완료된 사람
#             if receptions[i][1] == 1:
#                 # 수리하러 넘겨준다.
#                 waiting.append(receptions[i][0])
#                 receptions[i] = []
#             else:
#                 receptions[i][1] -= 1
#
# def repair():
#     # repair 순회
#     for i in range(m):
#         # 비었으면 채운다.
#         if not waiting:
#             break
#
#         if not repairs[i]:
#             k = waiting.popleft()
#             repair_desk[i].append(k[0])
#             repairs[i] = [k, ai[i]]
#
#         else:
#             # 완료된 사람
#             if repairs[i][1] == 1:
#                 # 수리하러 넘겨준다.
#                 repairs[i] = []
#             else:
#                 repairs[i][1] -= 1
