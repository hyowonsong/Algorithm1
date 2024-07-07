# 프로세스

from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    answer = 0
    while q: 
        m = max(q)                # m = max(q) 정의해줘야
        l = q.popleft()           # 이거 빼줘야
        location -= 1             # 문서 하나가 빠졌기 때문에 location -=1 해준다.
        
        if l != m:                # l이 max(q)가 아닌 경우
            q.append(l)         
            if location < 0:      # 사용자가 요청한 문서의 위치가 큐를 벗어나는 경우를 처리
                location = len(q) -1 # 이런 경우에는 큐의 마지막에 위치한 문서로 위치를 갱신해야 합니다. 
        
        else:                     # l이 max(q)인 경우
            answer += 1
            if location < 0:      # location이 0 이하로 떨어진다면, 이는 큐의 왼쪽 끝을 벗어나는 것을 의미합니다.
                break
            
    return answer