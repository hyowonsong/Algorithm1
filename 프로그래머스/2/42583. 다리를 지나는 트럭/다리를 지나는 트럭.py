from collections import deque

def solution(bridge_length, weight, truck_weights):
    queue = deque(truck_weights)  # 대기 중인 트럭 리스트를 큐로 변환
    bridge = deque([0] * bridge_length)  #다리 위 상태(초기에는 비어있음)
    total_weight = 0  # 현재 다리 위 트럭들의 무게 합
    time = 0  # 경과 시간
    
    # queue가 돌아가거나 total_weight이 0보다 크면
    while queue or total_weight > 0:
        time += 1
        # 2. 다리에서 트럭이 나옴
        exiting_truck = bridge.popleft()
        total_weight -= exiting_truck

        # 1. 다리에 트럭을 올릴 수 있는지 확인
        if queue and total_weight + queue[0] <= weight:
            entering_truck = queue.popleft()
            bridge.append(entering_truck)
            total_weight += entering_truck
        else:
            bridge.append(0)  # 트럭이 없으면 빈 자리 유지
            
    return time
