from heapq import heappop, heappush

def solution(scoville, K):
    heap = []
    answer = 0

    # 모든 스코빌 지수를 힙에 추가
    for s in scoville:
        heappush(heap, s)
    
    # 힙의 최소값이 K 이상이 될 때까지 반복
    while heap[0] < K:
        # 힙에 원소가 두 개 이상 있어야 함
        if len(heap) < 2:
            return -1
        
        # 가장 맵지 않은 두 개의 음식을 꺼내서 섞음
        first = heappop(heap)
        second = heappop(heap)
        new_scoville = first + 2 * second
        
        # 새로 만든 음식을 힙에 추가
        heappush(heap, new_scoville)
        answer += 1

    return answer
