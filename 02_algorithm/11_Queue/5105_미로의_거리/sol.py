'''
bfs 사용하여
현재 노드에서 움직일 수 있는 모든 노드로 이동
(visited에 이동한 거리 적어주기)
도착지에 도착하면 이동 거리 출력
도착지에 도착하지 못하면 0 출력
'''
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    print(f'#{tc}', end=' ')
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 출발점 찾기(a, b)
    a = b = 0
    for i in range(N):
        if 2 in arr[i]:
            a = i
            b = arr[i].index(2)

    result = 0
    q = [[a, b]]
    visited[a][b] = 1
    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    # 탐색
    while q:
        t = q.pop(0)
        for d in range(4):
            if 0 <= t[0]+di[d] < N and 0 <= t[1]+dj[d] < N:
                if arr[t[0]+di[d]][t[1]+dj[d]] == 3:
                    result = visited[t[0]][t[1]]-1
                elif arr[t[0]+di[d]][t[1]+dj[d]] != 1 and visited[t[0]+di[d]][t[1]+dj[d]] == 0:
                    q.append([t[0]+di[d], t[1]+dj[d]])
                    visited[t[0]+di[d]][t[1]+dj[d]] = visited[t[0]][t[1]]+1
    print(result)