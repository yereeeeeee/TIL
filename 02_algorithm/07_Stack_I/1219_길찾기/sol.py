import sys
sys.stdin = open('input.txt')

def DFS():

T = int(input())
for tc in range(1, T+1):
    length = int(input())
    visited = [0] * length

