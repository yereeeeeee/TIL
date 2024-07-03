from collections import deque

def solution(land):
    answer = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    n = len(land)
    m = len(land[0])
    
    visited = [[0] * m for _ in range(n)]
    
    size = {}
    num = 1
    def bfs(i, j):
        q = deque([(i, j)])
        visited[i][j] = num
        visit_list = [(i, j)]
        size_value = 1

        while q:
            x, y = q.popleft()
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0 <= nx < n and 0 <= ny < m and land[nx][ny] and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = num
                    visit_list.append((nx, ny))
                    size_value += 1

        for pos in visit_list:
            size[pos] = size_value
    
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                bfs(i, j)
                num += 1

    for j in range(m):
        tmp = 0
        cnt = 0
        for i in range(n):
            if land[i][j] and visited[i][j] != tmp:
                tmp = visited[i][j]
                cnt += size[(i, j)]
                
        answer = max(cnt, answer)
        
    # print(visited)
    return answer

print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))
print(solution([[1, 0, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0], [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 0], [1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]]))