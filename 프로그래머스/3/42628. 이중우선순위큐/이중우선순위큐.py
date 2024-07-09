from heapq import heappush, heappop

def solution(operations):
    min_heap = []  # 최소 힙을 저장할 리스트
    max_heap = []  # 최대 힙을 저장할 리스트 (음수 값을 저장하여 최대 힙으로 사용)

    for operation in operations:
        order, number = operation.split()
        number = int(number)

        if order == "I":
            # 숫자를 최소 힙과 최대 힙에 각각 추가
            heappush(min_heap, number)
            heappush(max_heap, -number)
        elif order == "D":
            if number == 1 and max_heap:
                # 최대값을 삭제하는 경우: 최대 힙에서 값을 꺼내고, 해당 값을 최소 힙에서 제거
                max_value = -heappop(max_heap)
                min_heap.remove(max_value)
            elif number == -1 and min_heap:
                # 최소값을 삭제하는 경우: 최소 힙에서 값을 꺼내고, 해당 값을 최대 힙에서 제거
                min_value = heappop(min_heap)
                max_heap.remove(-min_value)

    # 모든 연산을 처리한 후
    if min_heap and max_heap:
        # 최소 힙과 최대 힙이 비어있지 않으면 최대값과 최소값 반환
        return [-max_heap[0], min_heap[0]]
    else:
        # 둘 중 하나라도 비어있으면 [0, 0] 반환
        return [0, 0]
