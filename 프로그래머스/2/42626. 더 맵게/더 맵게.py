import heapq 

def solution(scoville, K):
    # 최소 힙 초기화
    heapq.heapify(scoville)
    
    answer = 0
    
    while scoville[0] < K:
        # 만약 힙의 길이가 1이고 첫번째 요소가 K보다 작다면
        if len(scoville) == 1:
            return -1
        
        # 가장 작은 두 요소 꺼내기
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        
        # 새로운 음식의 스코빌 지수 계산
        new_food = first + (second * 2)
        
        # 새로운 음식을 힙에 추가
        heapq.heappush(scoville, new_food)
        
        answer += 1

    return answer
