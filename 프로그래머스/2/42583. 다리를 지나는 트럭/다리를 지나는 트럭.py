from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 대기 트럭 큐
    trucks = deque(truck_weights)
    # 다리 큐 (다리 위의 트럭과 다리 진입 시간을 기록)
    bridge = deque()
    total_weight = 0  # 현재 다리 위의 총 무게
    time = 0  # 경과 시간

    while trucks or bridge:
        time += 1
        
        # 다리를 다 건넌 트럭을 다리에서 내리기
        if bridge and bridge[0][1] + bridge_length == time:
            total_weight -= bridge.popleft()[0]
        
        # 다리에 트럭 올리기
        if trucks and total_weight + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append((truck, time))
            total_weight += truck
    
    return time
