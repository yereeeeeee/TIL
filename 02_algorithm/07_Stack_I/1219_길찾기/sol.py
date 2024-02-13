import sys
sys.stdin = open('input.txt')

def DFS(start, end):
    visited = [0] * (end*1)
    stack = []
    visited[start] = 1
    while True:
        for w in adjl[start]:
            if visited[w] == 0:
                stack.append(start)
                start = w
                visited[w] = 1
                print(start)
                break
            else:
                if stack:
                    start = stack.pop()
                else:
                    break


tc, length = map(int, input().split())
num_set = list(map(int, input().split()))
N_list = list(sorted(num_set))
N = N_list[-2]
adjl = [[] for _ in range(N+1)]

for i in range(length):
    adjl[num_set[i*2]].append(num_set[i*2+1])

print(DFS(0, 99))