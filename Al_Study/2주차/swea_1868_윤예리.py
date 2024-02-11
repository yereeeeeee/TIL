import pprint

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    print(arr)
    answer = [[0] * N+2 for _ in range(N+2)]
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '*':
                answer[i][j] = '*'

    

    for i in range(N):
        for j in range(N):
            if answer[i][j] == 0:
                if 
        
    pprint.pprint(answer)
