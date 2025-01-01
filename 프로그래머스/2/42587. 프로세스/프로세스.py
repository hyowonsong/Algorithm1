from collections import deque

def solution(priorities, location):
    # 큐 초기화 (리스트를 하나씩 큐에 추가)
    queue = deque()
    for index,prioritie in enumerate(priorities):
        queue.append((index, prioritie))

    answer = 0 

    while queue:
        current = queue.popleft()

        # 큐에 있는 다른 프로세스 중 더 높은 우선순위가 있는지 확인
        valid = False
        for i in queue:
            if i[1]> current[1]:
                valid = True
                break
        
        # 더 높은 우선순위가 있으면 다시 큐에 삽입
        if valid :
            queue.append(current)
        # 더 높은 우선순위가 없고 current 가 가장 크다면 프로세스를 실행
        else:
            answer += 1
            if current[0] == location:
                # 목표 프로세스가 실행될 순서를 반환
                return answer