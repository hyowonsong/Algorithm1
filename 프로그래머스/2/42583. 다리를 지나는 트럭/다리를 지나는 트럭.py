from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 대기 트럭 큐
    queue = deque(truck_weights)
    # 다리 큐 (다리 위의 트럭과 다리 진입 시간을 기록)
    bridge_queue = deque()
    total_weight = 0  # 현재 다리 위의 총 무게
    time = 0  # 경과 시간
    
    # 대기 트럭 큐이거나 다리 큐 이면은 +1
    while queue or bridge_queue:
        time += 1
        
        # "현재 시간이 (트럭의 진입 시간 + 다리 길이)와 같다면, 
        # 그 트럭은 다리를 완전히 건넌 것이므로 다리에서 제거한다"
        if bridge_queue and bridge_queue[0][1] + bridge_length==time:
            total_weight -= bridge_queue.popleft()[0]
            
        # 대기 중인 트럭 있고, 새 트럭을 올려도 무게 제한을 초과X
        if queue and total_weight + queue[0] <= weight:
            # 대기 큐에서 첫 번째 트럭을 꺼냄(truck 정의)
            truck = queue.popleft()  
            # 다리 큐에 (트럭 무게, 현재 시간) 튜플 추가
            bridge_queue.append((truck, time))  
            # 다리 위 총 무게 갱신(앞에서 정의한 truck 추가)
            total_weight += truck 
    
    return time
