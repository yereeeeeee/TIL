# dfs 백트래킹 안됨

def check():
    start = 0
    end = n

    while start <= end:
        mid = (start+end)//2
        if arr[mid] <= c:
            start = mid + 1
        else:
            end = mid
        

n, c = map(int, input().split())
arr = sorted(list(map(int, input().split())))

# https://supersfel.tistory.com/249