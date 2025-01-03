# 더 맵게
from heapq import *

def solution(scoville, k):
    answer = 0
    min_heap = []

    # 모든 스코빌 지수를 힙에 추가
    for s in scoville:
        heappush(min_heap, s)

    # 힙의 최소값이 K 이상이 될 때까지 반복
    for s in scoville:
        while min_heap[0] < k:
            # 힙에 원소가 두 개 이상 있어야 함
            if len(min_heap)<2:
                return -1 
            
            else:
                # 가장 맵지 않은 두 개의 음식을 꺼내서 섞음
                first = heappop(min_heap)
                second = heappop(min_heap)
                new_scoville = first + 2* second

                # 새로 만든 음식을 힙에 추가
                heappush(min_heap, new_scoville)
                answer += 1

    return answer