from collections import deque

def solution(x, y, n):
    # 방문 여부를 저장하기 위한 리스트 (y + 1까지 초기화)
    visited = [False] * (y + 1)
    # BFS를 위한 큐 초기화
    queue = deque([(x, 0)])
    visited[x] = True  # 시작 숫자 방문 처리
    
    while queue:
        current, current_count = queue.popleft()
        
        # 목표 숫자에 도달한 경우 연산 횟수를 반환
        if current == y:
            return current_count
        
        # 다음 상태로 이동 가능한 경우들을 탐색
        next_states = [current + n, current * 2, current * 3]
        
        for next_state in next_states:
            # 목표 숫자를 초과하지 않고, 아직 방문하지 않은 상태인 경우 큐에 추가
            if next_state <= y and not visited[next_state]:
                visited[next_state] = True
                queue.append((next_state, current_count + 1))
    
    # 목표 숫자에 도달할 수 없는 경우 -1 반환
    return -1
