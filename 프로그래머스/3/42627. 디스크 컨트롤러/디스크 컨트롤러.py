from heapq import *

def solution(jobs):
    # 작업 요청 시간을 기준으로 정렬
    jobs.sort(key=lambda x: x[0])
    
    current = 0
    total = 0
    index = 0
    queue = []
    
    while index < len(jobs) or queue:
        # 현재 시간에 요청된 작업을 대기 큐에 추가
        while index < len(jobs) and jobs[index][0] <= current:
            heappush(queue, (jobs[index][1], jobs[index][0]))  # (소요 시간, 요청 시각)
            index += 1
        
        if queue:
            # 대기 큐에서 가장 우선순위가 높은 작업 꺼내기
            duration, request_time = heappop(queue)
            current += duration
            total += current - request_time
        else:
            # 대기 큐가 비어있다면 다음 작업 요청 시간으로 건너뜀
            current = jobs[index][0]
    
    # 반환 시간 평균의 정수 부분 반환
    return total // len(jobs)
