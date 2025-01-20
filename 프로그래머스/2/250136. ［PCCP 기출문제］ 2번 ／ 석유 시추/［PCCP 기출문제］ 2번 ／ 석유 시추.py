from collections import deque

def find_oil_chunk(land, visited, start_x, start_y, n, m):
    # land (List[List[int]]): 땅의 정보를 담은 2차원 배열
    # visited (List[List[bool]]): 방문 여부를 체크하는 2차원 배열
    # start_x (int): 시작점의 x 좌표
    # start_y (int): 시작점의 y 좌표
    # n (int): 땅의 세로 길이
    # m (int): 땅의 가로 길이
    
    # return Tuple[int, Set[int]]: (덩어리의 크기, 덩어리가 포함된 열들의 집합)

    chunk_size = 0
    columns = set()  # 이 덩어리가 포함된 열들
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = True
    
    while queue:
        x, y = queue.popleft()
        chunk_size += 1
        columns.add(y)
        
        # 4방향 탐색 (상하좌우)
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (0 <= nx < n and 0 <= ny < m and 
                not visited[nx][ny] and land[nx][ny] == 1):
                visited[nx][ny] = True
                queue.append((nx, ny))
                
    return chunk_size, columns

# 시추관을 설치했을 때 얻을 수 있는 최대 석유량을 계산하는 함수
def solution(land):
    n, m = len(land), len(land[0])
    visited = [[False] * m for _ in range(n)]
    oil_chunks = {}  # 석유 덩어리의 크기를 저장하는 딕셔너리
    chunk_id = 0
    
    # 각 열이 어떤 덩어리들에 접근할 수 있는지 저장하는 리스트
    column_to_chunks = [set() for _ in range(m)]
    
    # 모든 석유 덩어리 찾기
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and land[i][j] == 1:
                size, columns = find_oil_chunk(land, visited, i, j, n, m)
                oil_chunks[chunk_id] = size
                # 각 열에 이 덩어리 매핑
                for col in columns:
                    column_to_chunks[col].add(chunk_id)
                chunk_id += 1
    
    # 각 열에서 얻을 수 있는 최대 석유량 계산
    max_oil = 0
    for col in range(m):
        # 현재 열(col)에서 접근 가능한 모든 덩어리들의 석유량 합산
        total_oil = 0
        for chunk_id in column_to_chunks[col]:
            chunk_size = oil_chunks[chunk_id]  # 현재 덩어리의 크기
            total_oil += chunk_size
        max_oil = max(max_oil, total_oil)
    
    return max_oil