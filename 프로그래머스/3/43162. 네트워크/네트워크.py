from collections import deque

def bfs(computers, visited, start):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        current = queue.popleft()
        for i in range(len(computers)): 
            if computers[current][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    visited = [False] * n
    
    for i in range(n):
        if not visited[i]:
            bfs(computers, visited, i)
            answer += 1
            
    return answer