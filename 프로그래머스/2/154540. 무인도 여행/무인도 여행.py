def solution(maps):
    def iterative_dfs(start_x, start_y):
        stack = [(start_x, start_y)]
        total = 0
        while stack:
            x, y = stack.pop()
            if x < 0 or x >= len(maps) or y < 0 or y >= len(maps[0]):
                continue
            if maps[x][y] == 'X' or visited[x][y]:
                continue
            
            visited[x][y] = True
            total += int(maps[x][y])
            
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                stack.append((x + dx, y + dy))
        
        return total

    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    islands = []

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                islands.append(iterative_dfs(i, j))

    return sorted(islands) if islands else [-1]