# 프로세스
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)

    
    while queue:
        # max(queue) 를 지정해줘야 한다.
        m = max(queue)
        # 실행 대기 큐에서 대기중인 프로세스 하나를 꺼낸다.
        l = queue.popleft()
        # 문서 하나가 빠졌기 때문에 location -= 1 해준다.
        location -= 1

        # 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 
        # 꺼냈던 프로세스를 다시 넣고
        # 사용자가 요청한 문서의 위치가 큐를 벗어나는 경우를 처리해준다.
        if l != m:
            queue.append(l)
            if location < 0:
                location = len(queue)- 1

        else:
            answer += 1
            # location이 0 이하로 떨어진다면, 이는 큐의 왼쪽 끝을 벗어나는 것을 의미
            if location < 0:
                break
    return answer