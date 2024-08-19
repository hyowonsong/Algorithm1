from collections import deque

def solution(priorities, location):
    # 큐 초기화 (리스트를 하나씩 큐에 추가)
    queue = deque()
    for idx, value in enumerate(priorities):
        queue.append((value, idx))
    
    order = 0
    
    while queue:
        current = queue.popleft()
        
        # 큐에 있는 다른 프로세스 중 더 높은 우선순위가 있는지 확인
        has_higher_priority = False
        for i in queue:
            if current[0] < i[0]:
                has_higher_priority = True
                break
        
        # 더 높은 우선순위가 있으면 다시 큐에 삽입
        if has_higher_priority:
            queue.append(current)  
        # 더 높은 우선순위가 없고 current 가 가장 크다면 프로세스를 실행
        else:
            order += 1  
            if current[1] == location:
                return order  # 목표 프로세스가 실행될 순서를 반환
                