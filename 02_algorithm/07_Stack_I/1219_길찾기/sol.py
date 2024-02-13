import sys
sys.stdin = open('input.txt')

# def DFS():

tc, length = map(int, input().split())
num_set = list(map(int, input().split()))
N = min(99, max())
visited_1 = [0] * (N+1)
visited_2 = [0] * (N+1)

for num in range(length):
    if visited_1[num_set[num*2]] == 0:
        visited_1[num_set[num*2]] = num_set[num*2+1]
    else:
        visited_2[num_set[num * 2]] = num_set[num * 2 + 1]



    print(visited_1)
    print(visited_2)